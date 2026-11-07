

import typing

BuildState = typing.Union[
    typing.Literal["missing", "in_progress", "build_completed", "completed", "failed"], typing.Any
]
