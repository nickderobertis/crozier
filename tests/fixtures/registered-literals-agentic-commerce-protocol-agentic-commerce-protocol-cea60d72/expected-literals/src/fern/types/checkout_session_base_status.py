

import typing

CheckoutSessionBaseStatus = typing.Union[
    typing.Literal[
        "not_ready_for_payment", "ready_for_payment", "completed", "canceled", "in_progress", "authentication_required"
    ],
    typing.Any,
]
