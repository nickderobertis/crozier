

import typing

ObExternalAccountSubType1Code = typing.Union[
    typing.Literal[
        "ChargeCard", "CreditCard", "CurrentAccount", "EMoney", "Loan", "Mortgage", "PrePaidCard", "Savings"
    ],
    typing.Any,
]
