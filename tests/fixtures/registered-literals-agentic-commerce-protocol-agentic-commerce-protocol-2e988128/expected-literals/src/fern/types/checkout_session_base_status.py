

import typing

CheckoutSessionBaseStatus = typing.Union[
    typing.Literal[
        "not_ready_for_payment", "authentication_required", "ready_for_payment", "completed", "canceled", "in_progress"
    ],
    typing.Any,
]
