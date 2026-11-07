

import typing

ApprovalInteractionState = typing.Union[
    typing.Literal["required", "pending", "complete", "declined", "expired", "failed"], typing.Any
]
