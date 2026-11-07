

import typing

SearchUsingAttributeRequestTimeRangeType = typing.Union[
    typing.Literal[
        "CUSTOM",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_MONTH",
        "THIS_MONTH",
        "TODAY",
        "YESTERDAY",
        "THIS_YEAR",
        "LAST_YEAR",
        "THIS_QUARTER",
        "LAST_QUARTER",
        "LAST_3_MONTHS",
        "LAST_6_MONTHS",
        "LAST_12_MONTHS",
    ],
    typing.Any,
]
