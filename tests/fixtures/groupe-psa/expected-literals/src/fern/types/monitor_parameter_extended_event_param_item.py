

import typing

MonitorParameterExtendedEventParamItem = typing.Union[
    typing.Literal[
        "vehicle.doorsState",
        "vehicle.status",
        "vehicle.maintenance",
        "vehicle.position",
        "vehicle.telemetry",
        "vehicle.alerts",
        "vehicle.collisions",
        "vehicle.trip",
        "vehicle.stolen",
    ],
    typing.Any,
]
