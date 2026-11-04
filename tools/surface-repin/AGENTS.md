# surface-repin

The repin composition suite instruments a tiny dependency-free Rust workspace.
It runs the real CLIs and writers, with no dependency on crozier crate sources;
keep that edge absent so ordinary product changes do not trigger this journey.
Its actual instrumentation holds the host-wide measurement lock.
