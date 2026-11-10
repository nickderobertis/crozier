

import typing

PayPeriodDetailsPayFrequency = typing.Union[
    typing.Literal[
        "PAY_FREQUENCY_UNKNOWN",
        "PAY_FREQUENCY_WEEKLY",
        "PAY_FREQUENCY_BIWEEKLY",
        "PAY_FREQUENCY_SEMIMONTHLY",
        "PAY_FREQUENCY_MONTHLY",
    ],
    typing.Any,
]
