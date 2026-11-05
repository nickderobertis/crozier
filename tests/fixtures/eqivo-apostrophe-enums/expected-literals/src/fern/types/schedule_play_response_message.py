

import typing

SchedulePlayResponseMessage = typing.Union[
    typing.Literal[
        "Play Executed",
        "CallUUID Parameter Missing",
        "Sounds Parameter Missing",
        "Time Parameter Missing",
        "Time Parameter must be > 0",
        "Legs Parameter is Invalid",
        "Length Parameter must be a positive integer",
        "Sounds Parameter is Invalid",
        "Play Failed -- Call not found",
        "Play Failed",
    ],
    typing.Any,
]
