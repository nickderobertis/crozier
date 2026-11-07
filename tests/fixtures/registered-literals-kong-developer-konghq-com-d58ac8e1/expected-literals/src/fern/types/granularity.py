

import typing

Granularity = typing.Union[
    typing.Literal[
        "tenSecondly",
        "thirtySecondly",
        "minutely",
        "fiveMinutely",
        "tenMinutely",
        "thirtyMinutely",
        "hourly",
        "twoHourly",
        "twelveHourly",
        "daily",
        "weekly",
    ],
    typing.Any,
]
