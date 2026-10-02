

import typing

EventType = typing.Union[
    typing.Literal["viewer-request", "viewer-response", "origin-request", "origin-response"], typing.Any
]
