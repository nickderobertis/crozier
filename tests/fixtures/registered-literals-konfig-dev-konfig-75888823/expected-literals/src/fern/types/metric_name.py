

import typing

MetricName = typing.Union[
    typing.Literal["cpu", "memory", "rate_egress", "total_egress", "active_connections"], typing.Any
]
