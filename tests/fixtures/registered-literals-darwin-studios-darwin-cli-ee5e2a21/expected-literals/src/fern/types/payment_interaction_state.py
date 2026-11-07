

import typing

PaymentInteractionState = typing.Union[
    typing.Literal["required", "pending", "complete", "declined", "expired", "failed"], typing.Any
]
