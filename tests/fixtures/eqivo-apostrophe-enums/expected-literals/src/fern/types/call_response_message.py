

import typing

CallResponseMessage = typing.Union[
    typing.Literal[
        "Call Request Executed",
        "Mandatory Parameters Missing",
        "AnswerUrl is not Valid",
        "HangupUrl is not Valid",
        "RingUrl is not Valid",
        "Unknown Core UUID",
    ],
    typing.Any,
]
