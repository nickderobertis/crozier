

import typing

PresentationNetworkReadinessStatus = typing.Union[
    typing.Literal[
        "not_applicable",
        "network_manager_unavailable",
        "helper_missing",
        "helper_unhealthy",
        "unsupported",
        "wifi_adapter_unavailable",
        "unassigned",
        "reporting_pending",
        "connected",
        "failed",
        "configuration_pending",
        "ready",
    ],
    typing.Any,
]
