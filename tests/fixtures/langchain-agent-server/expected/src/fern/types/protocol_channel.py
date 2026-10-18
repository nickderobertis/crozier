

ProtocolChannel = str
"""
Subscribable event channel. One of the eight fixed channels or a user-defined `custom:<name>` namespaced custom channel emitted by a stream transformer. `debug` and `checkpoints` were removed from the protocol in `@langchain/protocol@0.0.10` — task-level debug info now flows on the `tasks` channel, and checkpoint pointers ride on `values` events as an attached `checkpoint` envelope.
"""
