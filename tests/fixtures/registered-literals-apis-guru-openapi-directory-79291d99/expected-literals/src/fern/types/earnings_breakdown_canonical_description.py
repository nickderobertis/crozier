

import typing

EarningsBreakdownCanonicalDescription = typing.Union[
    typing.Literal[
        "BONUS",
        "COMMISSION",
        "OVERTIME",
        "PAID TIME OFF",
        "REGULAR PAY",
        "VACATION",
        "BASIC ALLOWANCE HOUSING",
        "BASIC ALLOWANCE SUBSISTENCE",
        "OTHER",
    ],
    typing.Any,
]
