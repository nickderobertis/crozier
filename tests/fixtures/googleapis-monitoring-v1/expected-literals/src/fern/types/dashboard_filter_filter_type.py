

import typing

DashboardFilterFilterType = typing.Union[
    typing.Literal[
        "FILTER_TYPE_UNSPECIFIED",
        "RESOURCE_LABEL",
        "METRIC_LABEL",
        "USER_METADATA_LABEL",
        "SYSTEM_METADATA_LABEL",
        "GROUP",
    ],
    typing.Any,
]
