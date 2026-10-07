# fern-refusals-strict

- `measure` records crozier's `--fern-strict` exit, so this suite builds crozier
  and drives `fern-refusals.py measure` and `build` with that binary. It is the
  one fern-refusals suite that needs the crate, so it declares `crozier` as a
  dependency and the offline `fern-refusals` project does not.
- It runs `measure` from a scratch checkout holding exactly the modules it loads
  (`MEASURE_LOADS`); a module `measure` starts loading goes there and into
  `test`'s inputs together. No case runs Fern or reaches the network: the
  probe is screened by its committed `fern check` log.
