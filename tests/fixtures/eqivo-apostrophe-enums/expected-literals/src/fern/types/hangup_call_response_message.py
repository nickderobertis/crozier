

import typing

HangupCallResponseMessage = typing.Union[
    typing.Literal[
        "Hangup Call Executed",
        "CallUUID or RequestUUID Parameter must be present",
        "Both CallUUID and RequestUUID Parameters cannot be present",
        "Hangup Call Failed",
    ],
    typing.Any,
]
