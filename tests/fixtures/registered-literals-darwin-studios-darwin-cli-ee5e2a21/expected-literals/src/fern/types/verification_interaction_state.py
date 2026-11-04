

import typing

VerificationInteractionState = typing.Union[
    typing.Literal["required", "pending", "succeeded", "failed", "inconclusive", "expired"], typing.Any
]
