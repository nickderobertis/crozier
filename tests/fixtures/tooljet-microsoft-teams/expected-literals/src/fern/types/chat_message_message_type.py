

import typing

ChatMessageMessageType = typing.Union[
    typing.Literal["message", "chatEvent", "typing", "unknownFutureValue", "systemEventMessage"], typing.Any
]
