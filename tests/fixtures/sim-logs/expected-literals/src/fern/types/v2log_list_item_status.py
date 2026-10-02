

import typing

V2LogListItemStatus = typing.Union[
    typing.Literal["pending", "running", "paused", "redacting", "completed", "failed", "cancelled"], typing.Any
]
