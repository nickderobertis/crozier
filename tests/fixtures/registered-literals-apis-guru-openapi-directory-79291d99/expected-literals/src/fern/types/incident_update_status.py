

import typing

IncidentUpdateStatus = typing.Union[
    typing.Literal["INVESTIGATING", "IDENTIFIED", "SCHEDULED", "RESOLVED", "UNKNOWN"], typing.Any
]
