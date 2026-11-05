

import typing

TransferCallResponseMessage = typing.Union[
    typing.Literal[
        "Transfer Call Executed",
        "CallUUID Parameter must be present",
        "Url Parameter must be present",
        "Url is not Valid",
        "Transfer Call Failed -- Call not found",
        "Transfer Call Failed",
    ],
    typing.Any,
]
