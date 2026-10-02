

import typing

JobResultStatusLabel = typing.Union[
    typing.Literal["Pending", "Scheduled", "Running", "Completed", "Errored", "Failed"], typing.Any
]
