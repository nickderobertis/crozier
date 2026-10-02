

import typing

DbMigrationState = typing.Union[
    typing.Literal[
        "pending",
        "above_target",
        "below_baseline",
        "baseline",
        "ignored",
        "missing_success",
        "missing_failed",
        "success",
        "undone",
        "available",
        "failed",
        "out_of_order",
        "future_success",
        "future_failed",
        "outdated",
        "superseded",
        "deleted",
    ],
    typing.Any,
]
