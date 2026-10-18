

import typing

OrganizationProjectsResponseOutputProjectsItemStatus = typing.Union[
    typing.Literal[
        "INACTIVE",
        "ACTIVE_HEALTHY",
        "ACTIVE_UNHEALTHY",
        "COMING_UP",
        "UNKNOWN",
        "GOING_DOWN",
        "INIT_FAILED",
        "REMOVED",
        "RESTORING",
        "UPGRADING",
        "PAUSING",
        "RESTORE_FAILED",
        "RESTARTING",
        "PAUSE_FAILED",
        "RESIZING",
    ],
    typing.Any,
]
