

import typing

TransactionFullSimpleStatus = typing.Union[
    typing.Literal[
        "SUCCESSFUL",
        "PAID_OUT",
        "CANCEL_FAILED",
        "CANCELLED",
        "CHARGEBACK",
        "FAILED",
        "REFUND_FAILED",
        "REFUNDED",
        "NON_COLLECTION",
        "PENDING",
    ],
    typing.Any,
]
