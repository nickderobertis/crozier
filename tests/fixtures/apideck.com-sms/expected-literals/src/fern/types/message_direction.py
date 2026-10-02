

import typing

MessageDirection = typing.Union[
    typing.Literal["inbound", "outbound-api", "outbound-call", "outbound-reply", "unknown"], typing.Any
]
