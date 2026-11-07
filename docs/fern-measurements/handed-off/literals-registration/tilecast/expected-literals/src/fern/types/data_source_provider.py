

import typing

DataSourceProvider = typing.Union[
    typing.Literal[
        "calendar", "rss", "atom", "json", "csv", "manual", "weather", "transit", "cap_alerts", "air_quality"
    ],
    typing.Any,
]
