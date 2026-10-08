

import typing

TelemetryEnumItem = typing.Union[
    typing.Literal[
        "environment",
        "privacy",
        "vehicle",
        "vehicle.adas",
        "vehicle.battery",
        "vehicle.doorsState",
        "vehicle.energies",
        "vehicle.engines",
        "vehicle.ignition",
        "vehicle.lighting",
        "vehicle.lightingSystem",
        "vehicle.safety",
        "vehicle.transmission",
        "vehicle.drivingBehavior",
        "vehicle.alarm.status",
        "vehicle.alarm.trigger",
        "vehicle.wipingBlades",
    ],
    typing.Any,
]
