

import typing

SoundTouchStopResponseMessage = typing.Union[
    typing.Literal[
        "SoundTouchStop Executed",
        "CallUUID Parameter Missing",
        "SoundTouchStop Failed -- Call not found",
        "SoundTouchStop Failed",
    ],
    typing.Any,
]
