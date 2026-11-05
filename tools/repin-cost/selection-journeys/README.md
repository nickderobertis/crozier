# base-carries selection journeys

Two real runs of the harness over this host's runs root (all 50 runs whose plan names crozier),
cut off at the baseline's `--until`. Each directory holds that run's `changes.tsv`,
`excluded.tsv` and `summary.md`.

- **A** — `python3 tools/repin-cost/repin_cost.py --window base-carries:6302409297c5f81b34b7884207d2029a02dbd508 --until 2026-11-02T12:30:01Z --out tools/repin-cost/selection-journeys/A`
  (`6302409297c5f81b34b7884207d2029a02dbd508` is #722's squash commit on main). Included: #725, #726, #728, whose heads as of the cutoff
  were cut from or merged a main carrying it (base `6302409297c5`). Excluded: #722 itself, and #723,
  #724 and #727 (base `6b4509ab9c00`). #724's head *today* carries the commit, because it merged main
  after the cutoff; its last head pushed before the cutoff (`f2ef64fec5cd`) does not, so it is excluded.
- **B** — the same with `--window base-carries:4c2f0920ae8b8d677c57fb815278185b790bff1a`, #722's own branch head. The superseded
  rule (the required commit is an ancestor of the change's final head) admits #722, because that head
  *is* the commit. The base rule excludes it: `base 6b4509ab9c00 lacks 4c2f0920ae8b (the branch's own
  commits carry 4c2f0920ae8b)`. No change is included.

Both runs made 0 uncached GitHub calls. To re-run, use the command shown; outputs other than
these three files go to `github-evidence/`, which is not committed.
