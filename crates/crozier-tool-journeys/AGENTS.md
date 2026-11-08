# crozier-tool-journeys

- The Action, major-tag and migration journeys, and the check that the hand-written gate
  stays out of the golden tier. Split from `crozier-e2e` so an edit to those surfaces never
  pays for the golden suite; a journey that reads a golden belongs there instead.
- Each file a journey reads is in `toolJourneyReads` (`nx.json`): an input is also the
  affected trigger, so a missing one means the suite silently stops rerunning.
- Run it through its target: the binary is the one `crozier:build` leaves beside `deps/`.
