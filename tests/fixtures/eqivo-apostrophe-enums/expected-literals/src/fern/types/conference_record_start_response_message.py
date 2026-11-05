

import typing

ConferenceRecordStartResponseMessage = typing.Union[
    typing.Literal[
        "Conference RecordStart Executed",
        "ConferenceName Parameter must be present",
        "FileFormat Parameter must be",
        "Conference RecordStart Failed",
        "Conference RecordStart Failed -- Conference not found",
    ],
    typing.Any,
]
