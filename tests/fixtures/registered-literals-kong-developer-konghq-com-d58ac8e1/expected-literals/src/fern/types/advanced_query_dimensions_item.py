

import typing

AdvancedQueryDimensionsItem = typing.Union[
    typing.Literal[
        "api",
        "api_product",
        "api_product_version",
        "application",
        "consumer",
        "control_plane",
        "control_plane_group",
        "data_plane_node",
        "data_plane_node_version",
        "gateway_service",
        "portal",
        "response_source",
        "route",
        "status_code",
        "status_code_grouped",
        "time",
        "upstream_status_code",
        "upstream_status_code_grouped",
    ],
    typing.Any,
]
