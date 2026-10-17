

import typing

ThreadSearchRequestSelectItem = typing.Union[
    typing.Literal[
        "thread_id",
        "created_at",
        "updated_at",
        "state_updated_at",
        "metadata",
        "config",
        "status",
        "values",
        "interrupts",
    ],
    typing.Any,
]
