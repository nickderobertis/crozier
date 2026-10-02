

import typing

N1N2MessageTransferCause = typing.Union[
    typing.Literal[
        "ATTEMPTING_TO_REACH_UE",
        "N1_N2_TRANSFER_INITIATED",
        "WAITING_FOR_ASYNCHRONOUS_TRANSFER",
        "UE_NOT_RESPONDING",
        "N1_MSG_NOT_TRANSFERRED",
        "UE_NOT_REACHABLE_FOR_SESSION",
    ],
    typing.Any,
]
