

import typing

RunObjectStatus = typing.Union[
    typing.Literal[
        "queued", "in_progress", "requires_action", "cancelling", "cancelled", "failed", "completed", "expired"
    ],
    typing.Any,
]
