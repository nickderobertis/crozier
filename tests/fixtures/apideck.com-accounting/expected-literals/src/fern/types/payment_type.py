

import typing

PaymentType = typing.Union[
    typing.Literal[
        "accounts_receivable",
        "accounts_payable",
        "accounts_receivable_credit",
        "accounts_payable_credit",
        "accounts_receivable_overpayment",
        "accounts_payable_overpayment",
        "accounts_receivable_prepayment",
        "accounts_payable_prepayment",
    ],
    typing.Any,
]
