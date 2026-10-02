

import typing

GetFamilyBalancesV3RequestMetricsItem = typing.Union[
    typing.Literal[
        "count",
        "sum_balance",
        "avg_balance",
        "min_balance",
        "max_balance",
        "sum_positive_balance",
        "sum_negative_balance",
        "count_zero_balance",
    ],
    typing.Any,
]
