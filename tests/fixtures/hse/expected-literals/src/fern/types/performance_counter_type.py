

import typing

PerformanceCounterType = typing.Union[
    typing.Literal["invalid", "basic", "rate", "latency", "distribution", "simple_latency"], typing.Any
]
