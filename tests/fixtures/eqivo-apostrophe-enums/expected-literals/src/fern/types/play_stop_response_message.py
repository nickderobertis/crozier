

import typing

PlayStopResponseMessage = typing.Union[
    typing.Literal[
        "PlayStop Executed", "CallUUID Parameter Missing", "PlayStop Failed -- Call not found", "PlayStop Failed"
    ],
    typing.Any,
]
