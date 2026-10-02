

import typing

JobStatus = typing.Union[
    typing.Literal["draft", "internal", "published", "completed", "on-hold", "private"], typing.Any
]
