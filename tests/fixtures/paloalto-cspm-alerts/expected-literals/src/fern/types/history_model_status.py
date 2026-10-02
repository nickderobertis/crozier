

import typing

HistoryModelStatus = typing.Union[
    typing.Literal["OPEN", "DISMISSED", "SNOOZED", "PENDING_RESOLUTION", "RESOLVED"], typing.Any
]
