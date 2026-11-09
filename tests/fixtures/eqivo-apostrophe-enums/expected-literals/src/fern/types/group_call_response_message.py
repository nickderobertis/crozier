

import typing

GroupCallResponseMessage = typing.Union[
    typing.Literal[
        "GroupCall Request Executed",
        "Mandatory Parameters Missing",
        "This Delimiter is not allowed",
        "GroupCall should be used for at least 2 numbers",
        "'To' parameter length does not match 'Gateways' Length",
        "AnswerUrl is not Valid",
        "HangupUrl is not Valid",
        "RingUrl is not Valid",
        "ConfirmSound is not Valid",
        "Unknown Core UUID",
        "GroupCall Request Failed",
    ],
    typing.Any,
]
