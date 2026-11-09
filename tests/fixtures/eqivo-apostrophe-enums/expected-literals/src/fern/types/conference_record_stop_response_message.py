

import typing

ConferenceRecordStopResponseMessage = typing.Union[
    typing.Literal[
        "Conference RecordStop Executed",
        "ConferenceName Parameter must be present",
        "RecordFile Parameter must be present",
        "Conference RecordStop Failed",
        "Conference RecordStop Failed -- Conference not found",
    ],
    typing.Any,
]
