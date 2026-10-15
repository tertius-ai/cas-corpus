# CAS Corpus agent guidance

This repository is the curated, public-ready corpus. It contains only
mathematics that executes against the exact Noether release named in each case.
The current accepted target is `tertius-noether==0.3.2`.

## Corpus boundary

- Do not commit incomplete, unsupported, aspirational, or rights-unclear
  material. Use an issue to propose additions before they enter the curated
  tree.
- Use only canonical public imports from `noether` and its nine domain modules.
  Never import `noether._engine` or invent future APIs.
- Python solutions are boundary programs, not alternate implementations of
  missing Noether mathematics.
- Keep coefficient contexts explicit. Do not guess coercions, presentations,
  precision, or randomness.
- Prefer object methods and standard Python protocols over duplicate helper
  functions.

## Cases

Each `cases/<domain>/<slug>/` directory has `case.json`, `README.md`, and
`solution.py`. The manifest must conform to `schemas/case.schema.json`.

Solutions import only Noether and the Python standard library. They must be
deterministic, bounded, executable without network access, and checked with
mathematical assertions or Noether evidence. Avoid wrappers that hide the
Noether API: the corpus is meant to demonstrate idiomatic use directly.

Write original explanatory prose. Preserve citations and translation history,
but do not copy third-party prose, figures, data, or notebooks unless their
redistribution basis has been reviewed and recorded in `case.json`.

Run `python3 tools/check_cases.py --execute` before committing a case.
