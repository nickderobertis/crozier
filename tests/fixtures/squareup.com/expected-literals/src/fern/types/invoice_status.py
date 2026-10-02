

import typing

InvoiceStatus = typing.Union[
    typing.Literal[
        "DRAFT",
        "UNPAID",
        "SCHEDULED",
        "PARTIALLY_PAID",
        "PAID",
        "PARTIALLY_REFUNDED",
        "REFUNDED",
        "CANCELED",
        "FAILED",
        "PAYMENT_PENDING",
    ],
    typing.Any,
]
