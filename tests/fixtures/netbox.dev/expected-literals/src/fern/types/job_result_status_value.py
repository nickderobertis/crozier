

import typing

JobResultStatusValue = typing.Union[
    typing.Literal["pending", "scheduled", "running", "completed", "errored", "failed"], typing.Any
]
