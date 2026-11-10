

import typing

TotalCanonicalDescription = typing.Union[
    typing.Literal[
        "BONUS",
        "COMMISSION",
        "OVERTIME",
        "PAID TIME OFF",
        "REGULAR PAY",
        "VACATION",
        "EMPLOYEE MEDICARE",
        "FICA",
        "SOCIAL SECURITY EMPLOYEE TAX",
        "MEDICAL",
        "VISION",
        "DENTAL",
        "NET PAY",
        "TAXES",
        "NOT_FOUND",
        "OTHER",
    ],
    typing.Any,
]
