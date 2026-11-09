

import typing

AuthenticationResultOutcome = typing.Union[
    typing.Literal["authenticated", "failed", "unavailable", "rejected", "attempt"], typing.Any
]
