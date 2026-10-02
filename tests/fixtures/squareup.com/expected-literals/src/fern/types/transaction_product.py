

import typing

TransactionProduct = typing.Union[
    typing.Literal[
        "REGISTER", "EXTERNAL_API", "BILLING", "APPOINTMENTS", "INVOICES", "ONLINE_STORE", "PAYROLL", "OTHER"
    ],
    typing.Any,
]
