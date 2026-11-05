

import typing

RecordStopResponseMessage = typing.Union[
    typing.Literal[
        "RecordStop Executed",
        "CallUUID Parameter must be present",
        "RecordFile Parameter must be present",
        "RecordStop Failed -- Call not found",
        "RecordStop Failed",
    ],
    typing.Any,
]
