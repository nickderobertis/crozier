

import typing

AuthenticationInteractionState = typing.Union[
    typing.Literal["required", "pending", "complete", "declined", "expired", "failed"], typing.Any
]
