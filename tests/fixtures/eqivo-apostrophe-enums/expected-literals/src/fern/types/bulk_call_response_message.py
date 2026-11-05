

import typing

BulkCallResponseMessage = typing.Union[
    typing.Literal[
        "BulkCalls Request Executed",
        "Mandatory Parameters Missing",
        "This Delimiter is not allowed",
        "BulkCalls should be used for at least 2 numbers",
        "'To' parameter length does not match 'Gateways' Length",
        "AnswerUrl is not Valid",
        "HangupUrl is not Valid",
        "RingUrl is not Valid",
        "Unknown Core UUID",
    ],
    typing.Any,
]
