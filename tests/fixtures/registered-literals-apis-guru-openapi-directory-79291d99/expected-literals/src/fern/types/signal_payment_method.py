

import typing

SignalPaymentMethod = typing.Union[
    typing.Literal[
        "SAME_DAY_ACH", "NEXT_DAY_ACH", "STANDARD_ACH", "REAL_TIME_PAYMENTS", "DEBIT_CARD", "MULTIPLE_PAYMENT_METHODS"
    ],
    typing.Any,
]
