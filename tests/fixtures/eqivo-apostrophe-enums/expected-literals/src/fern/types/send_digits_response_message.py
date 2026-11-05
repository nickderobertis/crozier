

import typing

SendDigitsResponseMessage = typing.Union[
    typing.Literal[
        "SendDigits Executed",
        "CallUUID Parameter Missing",
        "Digits Parameter Missing",
        "Invalid Leg Parameter",
        "SendDigits Failed -- Call not found",
        "SendDigits Failed",
    ],
    typing.Any,
]
