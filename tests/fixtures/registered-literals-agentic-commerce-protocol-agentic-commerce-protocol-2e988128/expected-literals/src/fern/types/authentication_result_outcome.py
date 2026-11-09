

import typing

AuthenticationResultOutcome = typing.Union[
    typing.Literal[
        "abandoned",
        "attempt_acknowledged",
        "authenticated",
        "canceled",
        "denied",
        "informational",
        "internal_error",
        "not_supported",
        "processing_error",
        "rejected",
    ],
    typing.Any,
]
