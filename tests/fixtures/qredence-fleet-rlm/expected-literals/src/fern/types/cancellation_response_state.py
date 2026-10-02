

import typing

CancellationResponseState = typing.Union[
    typing.Literal["requested", "already_requested", "already_terminal"], typing.Any
]
