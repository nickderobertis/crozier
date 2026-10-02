

import typing

ActionError = typing.Union[
    typing.Literal["not-authorized", "not-found", "invalid-name", "conflict", "request-too-large", "unknown"],
    typing.Any,
]
