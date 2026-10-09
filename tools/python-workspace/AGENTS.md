# python-workspace

- Tagged `type:tooling`, not `type:aggregate`: everything it depends on is
  tooling, and `workspace`'s supply-chain inputs glob every `tools/*/` directory,
  which the boundary rule reads as an edge from that aggregate into this one.
