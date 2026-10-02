

import typing

V2LogDetailStatus = typing.Union[
    typing.Literal["pending", "running", "paused", "redacting", "completed", "failed", "cancelled"], typing.Any
]
