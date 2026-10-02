

import typing

GetSpacesDetailedListV3RequestMetricsItem = typing.Union[
    typing.Literal[
        "sum_available_spaces",
        "sum_open_spaces",
        "sum_occupied_spaces",
        "sum_closed_spaces",
        "sum_unavailable_spaces",
        "capacity",
        "occupancy_rate",
    ],
    typing.Any,
]
