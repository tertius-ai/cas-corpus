# CAS Corpus

CAS Corpus is a curated collection of executable computer-algebra problems
translated to [Noether](https://github.com/tertius-ai/noether). Its purpose is
to provide useful mathematics, realistic feature coverage, and high-quality
examples of Noether's public API.

The current corpus target is exactly the source tag
[`tertius-noether v0.3.2`](https://github.com/tertius-ai/noether/tree/v0.3.2).
Every case in this repository must run against that release. Candidate
material, incomplete translations, unsupported mathematics, and feature
requests do not belong in the curated tree; open an issue to propose them.

The corpus contains 178 executable cases spanning eight Noether domains. The
complete index and short descriptions are in
[`cases/README.md`](cases/README.md).

## Case contract

Each case lives at `cases/<owning-domain>/<slug>/` and contains:

- `case.json`: provenance, rights, version, operation, and execution metadata;
- `README.md`: an original mathematical problem statement and translation
  notes;
- `solution.py`: an idiomatic executable using only Noether and the Python
  standard library.

Assertions should establish mathematical properties or verify returned
evidence. Stored output is explanatory, not the correctness oracle. Randomized
calculations must use and record an explicit seed.

Run structural checks with:

```bash
python3 tools/check_cases.py
```

Pull requests run these structural checks in GitHub Actions. They do not execute
the mathematics. Before merging case changes, also run the execution check below
against the exact Noether source release.

Noether 0.3.2 is a source-only release. Build that tag using its documented
`make sync && make engine` workflow, then invoke this repository's checker with
the resulting Python environment:

```bash
/path/to/noether/.venv/bin/python tools/check_cases.py --execute
```

## Publication boundary

Everything committed here must be suitable for publication.
Do not commit downloaded papers or notebooks merely because they are publicly
accessible. Include third-party source artifacts only when their redistribution
terms have been reviewed and recorded. A citation and an independently written
problem statement are the default.

## License

The original code, problem statements, and translation notes in this
repository are available under the [MIT License](LICENSE), copyright Benjamin
Antieau and Deven Manam. Cited third-party works are not redistributed here;
their citations and rights metadata do not alter their respective licenses.
