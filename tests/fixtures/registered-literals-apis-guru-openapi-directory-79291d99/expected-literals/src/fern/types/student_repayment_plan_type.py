

import typing

StudentRepaymentPlanType = typing.Union[
    typing.Literal[
        "extended graduated",
        "extended standard",
        "graduated",
        "income-contingent repayment",
        "income-based repayment",
        "interest-only",
        "other",
        "pay as you earn",
        "revised pay as you earn",
        "standard",
    ],
    typing.Any,
]
