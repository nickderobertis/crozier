

import typing

PostA2ARequestMethod = typing.Union[
    typing.Literal["message/send", "message/stream", "tasks/get", "tasks/cancel"], typing.Any
]
