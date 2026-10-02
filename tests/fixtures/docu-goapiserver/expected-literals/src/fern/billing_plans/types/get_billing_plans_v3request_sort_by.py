

import typing

GetBillingPlansV3RequestSortBy = typing.Union[
    typing.Literal[
        "sum_monthly_invoice_asc",
        "sum_monthly_invoice_desc",
        "avg_monthly_invoice_asc",
        "avg_monthly_invoice_desc",
        "count_students_asc",
        "count_students_desc",
        "group_asc",
        "group_desc",
    ],
    typing.Any,
]
