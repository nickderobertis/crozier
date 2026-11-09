

import typing

MetricsRelativeTimeRangeDtoV2TimeRange = typing.Union[
    typing.Literal[
        "15m", "1h", "6h", "12h", "24h", "7d", "30d", "current_week", "current_month", "previous_week", "previous_month"
    ],
    typing.Any,
]
