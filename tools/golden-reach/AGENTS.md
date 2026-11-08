# golden-reach

- The golden-reach suites, split from `surface-census` so an edit only the census reads
  never reruns them. Their inputs name the census scripts they load (the closure of
  `golden-reach.py`, `golden-reach-search.py`, `output-insensitive.py` and the census);
  a new script they load is an input here or it silently stops rerunning them.
- **`test-reach` and `test-reach-portable` keep their own runner** (a departure from
  `languages/python.md`'s pytest): see `tools/surface-census/AGENTS.md`.
