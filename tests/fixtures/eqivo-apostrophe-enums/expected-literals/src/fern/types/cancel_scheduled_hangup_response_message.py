

import typing

CancelScheduledHangupResponseMessage = typing.Union[
    typing.Literal[
        "Scheduled Hangup Cancelation Executed",
        "SchedHangupId Parameter must be present",
        "Scheduled Hangup Cancelation Failed -- ID not found",
        "Scheduled Hangup Cancelation Failed",
    ],
    typing.Any,
]
