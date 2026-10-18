

import typing

OrganizationProjectsResponseOutputProjectsItemDatabasesItemStatus = typing.Union[
    typing.Literal[
        "ACTIVE_HEALTHY",
        "ACTIVE_UNHEALTHY",
        "COMING_UP",
        "GOING_DOWN",
        "INIT_FAILED",
        "REMOVED",
        "RESTORING",
        "UNKNOWN",
        "INIT_READ_REPLICA",
        "INIT_READ_REPLICA_FAILED",
        "RESTARTING",
        "RESIZING",
    ],
    typing.Any,
]
