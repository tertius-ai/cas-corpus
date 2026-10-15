#!/usr/bin/env python3
"""Validate corpus manifests and optionally execute every curated case."""

from __future__ import annotations

import argparse
import ast
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases"
DOMAINS = {
    "linalg",
    "numthy",
    "commalg",
    "groups",
    "topology",
    "homalg",
    "combin",
    "geometry",
    "category",
}
STATUSES_THAT_ARE_NOT_LICENSES = {"", "unknown", "unreviewed", "tbd"}


class CaseError(Exception):
    """A corpus case violates the curated contract."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CaseError(message)


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise CaseError(f"cannot read {path.relative_to(ROOT)}: {error}") from error
    require(isinstance(value, dict), "case.json must contain a JSON object")
    return value


def validate_imports(path: Path) -> None:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as error:
        raise CaseError(f"cannot parse {path.relative_to(ROOT)}: {error}") from error
    standard = sys.stdlib_module_names
    for node in ast.walk(tree):
        names: list[str] = []
        if isinstance(node, ast.Import):
            names = [alias.name for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            require(node.level == 0 and node.module is not None,
                    f"{path.relative_to(ROOT)} uses a relative import")
            names = [node.module]
            if node.module == "noether":
                require(all(alias.name != "_engine" for alias in node.names),
                        f"{path.relative_to(ROOT)} imports private noether._engine")
        for name in names:
            root = name.partition(".")[0]
            require(
                root == "noether" or root in standard,
                f"{path.relative_to(ROOT)} imports disallowed package {root!r}",
            )
            require(name != "noether._engine" and not name.startswith("noether._engine."),
                    f"{path.relative_to(ROOT)} imports private noether._engine")


def validate_case(case_dir: Path) -> dict[str, Any]:
    manifest_path = case_dir / "case.json"
    readme = case_dir / "README.md"
    solution = case_dir / "solution.py"
    for required in (manifest_path, readme, solution):
        require(required.is_file(), f"missing {required.relative_to(ROOT)}")

    manifest = load_manifest(manifest_path)
    required_keys = {
        "schema_version", "id", "title", "domains", "source",
        "translation", "noether", "execution",
    }
    require(set(manifest) == required_keys, f"{manifest_path.relative_to(ROOT)} has wrong keys")
    require(manifest["schema_version"] == 1, "schema_version must be 1")
    require(isinstance(manifest["title"], str) and bool(manifest["title"].strip()),
            "title must be nonempty")

    relative = case_dir.relative_to(CASES)
    require(len(relative.parts) == 2, f"case must be at cases/<domain>/<slug>: {relative}")
    owner, slug = relative.parts
    require(owner in DOMAINS, f"unknown owning domain {owner!r}")
    require(manifest["id"] == f"{owner}.{slug}", "case id must match its directory")
    domains = manifest["domains"]
    require(isinstance(domains, list) and owner in domains, "domains must include the owner")
    require(len(domains) == len(set(domains)) and set(domains) <= DOMAINS,
            "domains must be unique accepted Noether domains")

    source = manifest["source"]
    require(isinstance(source, dict), "source must be an object")
    require(set(source) <= {
        "intake_id", "kind", "citation", "url", "license", "redistribution",
        "retrieved_at", "sha256",
    }, "source contains unknown keys")
    require({"kind", "citation", "url", "license", "redistribution"} <= set(source),
            "source is missing required keys")
    require(source["kind"] in {
        "paper", "notebook", "book", "documentation", "repository", "original"
    }, "source.kind is invalid")
    require(isinstance(source["citation"], str) and bool(source["citation"].strip()),
            "source.citation must be nonempty")
    require(source["url"] is None or isinstance(source["url"], str),
            "source.url must be a string or null")
    license_name = source.get("license")
    require(isinstance(license_name, str), "source.license must be a string")
    require(license_name.strip().lower() not in STATUSES_THAT_ARE_NOT_LICENSES,
            "curated cases require a reviewed source license or rights statement")
    require(source["redistribution"] in {"citation-only", "licensed-copy", "original"},
            "source.redistribution is invalid")
    digest = source.get("sha256")
    require(digest is None or (
        isinstance(digest, str)
        and len(digest) == 64
        and all(character in "0123456789abcdef" for character in digest)
    ), "source.sha256 must be a lowercase SHA-256 digest or null")

    translation = manifest["translation"]
    require(isinstance(translation, dict), "translation must be an object")
    require(set(translation) == {"kind", "notes"}, "translation has wrong keys")
    require(translation["kind"] in {"translation", "adaptation", "original"},
            "translation.kind is invalid")
    require(isinstance(translation["notes"], str), "translation.notes must be a string")

    noether = manifest["noether"]
    require(isinstance(noether, dict), "noether must be an object")
    require(noether.get("version") == "0.3.2", "current corpus target is Noether 0.3.2")
    operations = noether.get("operations")
    require(isinstance(operations, list) and operations, "declare at least one Noether operation")
    require(all(isinstance(value, str) for value in operations), "operations must be strings")
    require(len(operations) == len(set(operations)), "operations must be unique")

    execution = manifest["execution"]
    require(isinstance(execution, dict), "execution must be an object")
    require(execution.get("entrypoint") == "solution.py", "entrypoint must be solution.py")
    timeout = execution.get("timeout_seconds")
    require(isinstance(timeout, int) and 1 <= timeout <= 300,
            "timeout_seconds must be between 1 and 300")
    seed = execution.get("seed")
    require(seed is None or isinstance(seed, int), "seed must be an integer or null")

    validate_imports(solution)
    return manifest


def installed_noether() -> Any:
    try:
        import noether
    except ImportError as error:
        raise CaseError("--execute requires tertius-noether==0.3.2") from error
    require(noether.__version__ == "0.3.2",
            f"expected Noether 0.3.2, found {noether.__version__}")
    return noether


def execute_case(case_dir: Path, manifest: dict[str, Any], noether: Any) -> None:
    unsupported = [
        operation
        for operation in manifest["noether"]["operations"]
        if not noether.capabilities().supports(operation)
    ]
    require(not unsupported, f"unsupported declared operations: {', '.join(unsupported)}")
    environment = os.environ.copy()
    environment["PYTHONHASHSEED"] = "0"
    result = subprocess.run(
        [sys.executable, "-I", "solution.py"],
        cwd=case_dir,
        env=environment,
        text=True,
        capture_output=True,
        timeout=manifest["execution"]["timeout_seconds"],
        check=False,
    )
    require(
        result.returncode == 0,
        "solution failed "
        f"({result.returncode})\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}",
    )


def discover_cases() -> list[Path]:
    return sorted(path for path in CASES.glob("*/*") if path.is_dir())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true", help="check Noether APIs and run cases")
    arguments = parser.parse_args()
    cases = discover_cases()
    noether = installed_noether() if arguments.execute else None
    failures: list[str] = []
    seen: set[str] = set()
    for case_dir in cases:
        try:
            manifest = validate_case(case_dir)
            require(manifest["id"] not in seen, f"duplicate case id {manifest['id']}")
            seen.add(manifest["id"])
            if arguments.execute:
                execute_case(case_dir, manifest, noether)
            print(f"ok: {manifest['id']}")
        except (CaseError, subprocess.TimeoutExpired) as error:
            failures.append(f"{case_dir.relative_to(ROOT)}: {error}")
    if failures:
        print("\n".join(f"error: {failure}" for failure in failures), file=sys.stderr)
        return 1
    print(f"checked {len(cases)} curated case(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
