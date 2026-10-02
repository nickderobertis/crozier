

import typing

EcommerceOrderPaymentStatus = typing.Union[
    typing.Literal["pending", "authorized", "paid", "partial", "refunded", "voided", "unknown"], typing.Any
]
