

import typing

ScheduleHangupResponseMessage = typing.Union[
    typing.Literal[
        "ScheduleHangup Executed",
        "CallUUID Parameter must be present",
        "Time Parameter must be present",
        "Time Parameter must be > 0!",
        "ScheduleHangup Failed -- Call not found",
        "ScheduleHangup Failed",
    ],
    typing.Any,
]
