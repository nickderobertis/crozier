

import typing

TransferStatus = typing.Union[
    typing.Literal[
        "Initiated",
        "WaitingCounterparty",
        "WaitingSafeHeight",
        "WaitingConfirmations",
        "WaitingBroadcast",
        "Settled",
        "Failed",
    ],
    typing.Any,
]
