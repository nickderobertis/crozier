

import typing

ReconcileState = typing.Union[
    typing.Literal[
        "in_sync",
        "storage_ahead",
        "graph_ahead",
        "untracked",
        "missing_on_storage",
        "absent",
        "unreadable",
        "ungoverned",
        "ungoverned_live",
        "drop_observed",
    ],
    typing.Any,
]
