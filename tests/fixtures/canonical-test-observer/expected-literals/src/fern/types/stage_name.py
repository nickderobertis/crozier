

import typing

StageName = typing.Union[
    typing.Literal["proposed", "updates", "edge", "beta", "candidate", "stable", "pending", "current"], typing.Any
]
