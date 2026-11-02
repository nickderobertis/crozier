# fern-references-check

- A project of its own so crozier's pull-request gate runs
  `fern-references.py check` over the real tree exactly when a path it reads
  changes, and never for anything else. Its `test` inputs are that read set;
  `inventory_check_test.py` traces the check's own reads and fails naming any
  path no input covers, so a new read joins the inputs in the same change.
