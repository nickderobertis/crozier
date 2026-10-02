

import typing

CommandStatus = typing.Union[
    typing.Literal["QUEUED", "PROCESSING", "CANCELING", "SUCCEEDED", "FAILED", "CANCELED"], typing.Any
]
