

import typing

RecordStartResponseMessage = typing.Union[
    typing.Literal[
        "RecordStart Executed",
        "CallUUID Parameter must be present",
        "FileFormat Parameter must be",
        "RecordStart Failed: invalid TimeLimit",
        "RecordStart Failed -- Call not found",
        "RecordStart Failed",
    ],
    typing.Any,
]
