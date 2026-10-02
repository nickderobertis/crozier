

import typing

GetPaymentsV3RequestMetricsItem = typing.Union[
    typing.Literal[
        "count", "sum_amount", "sum_total_amount", "sum_fee_amount", "avg_amount", "avg_total_amount", "avg_fee_amount"
    ],
    typing.Any,
]
