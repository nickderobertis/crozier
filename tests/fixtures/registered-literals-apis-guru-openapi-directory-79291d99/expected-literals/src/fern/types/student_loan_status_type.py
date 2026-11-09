

import typing

StudentLoanStatusType = typing.Union[
    typing.Literal[
        "cancelled",
        "charged off",
        "claim",
        "consolidated",
        "deferment",
        "delinquent",
        "discharged",
        "extension",
        "forbearance",
        "in grace",
        "in military",
        "in school",
        "not fully disbursed",
        "other",
        "paid in full",
        "refunded",
        "repayment",
        "transferred",
    ],
    typing.Any,
]
