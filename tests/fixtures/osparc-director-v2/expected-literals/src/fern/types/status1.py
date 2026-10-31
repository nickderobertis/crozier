

import typing

Status1 = typing.Union[
    typing.Literal["created", "running", "paused", "restarting", "removing", "exited", "dead"], typing.Any
]
