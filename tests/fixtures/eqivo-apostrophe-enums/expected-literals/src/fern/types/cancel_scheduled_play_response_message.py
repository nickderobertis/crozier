

import typing

CancelScheduledPlayResponseMessage = typing.Union[
    typing.Literal[
        "Scheduled Play Cancelation Executed",
        "SchedPlayId Parameter must be present",
        "Scheduled Play Cancelation Failed -- ID not found",
        "Scheduled Play Cancelation Failed",
    ],
    typing.Any,
]
