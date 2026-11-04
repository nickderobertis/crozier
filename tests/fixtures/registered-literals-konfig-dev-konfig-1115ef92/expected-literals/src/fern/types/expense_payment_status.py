

import typing

ExpensePaymentStatus = typing.Union[
    typing.Literal[
        "NOT_STARTED",
        "PROCESSING",
        "CANCELED",
        "DECLINED",
        "CLEARED",
        "REFUNDING",
        "REFUNDED",
        "CASH_ADVANCE",
        "CREDITED",
        "AWAITING_PAYMENT",
        "SCHEDULED",
    ],
    typing.Any,
]
