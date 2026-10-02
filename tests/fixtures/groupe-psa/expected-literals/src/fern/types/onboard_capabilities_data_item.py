

import typing

OnboardCapabilitiesDataItem = typing.Union[
    typing.Literal[
        "data:vehicle:devices:pnc",
        "data:telemetry",
        "data:telemetry:environment",
        "data:telemetry:privacy",
        "data:telemetry:vehicle",
        "data:telemetry:vehicle:ignition",
        "data:telemetry:vehicle:preconditioning",
        "data:telemetry:vehicle:energies",
        "data:telemetry:vehicle:engines",
        "data:telemetry:vehicle:doorsState",
        "data:telemetry:vehicle:powertrain",
        "data:telemetry:vehicle:battery",
        "data:telemetry:vehicle:safety",
        "data:telemetry:vehicle:odometer",
        "data:telemetry:vehicle:kinetic",
        "data:telemetry:vehicle:transmission",
        "data:telemetry:vehicle:adas",
        "data:telemetry:vehicle:lightingSystem",
        "data:telemetry:vehicle:maintenance",
        "data:telemetry:vehicle:drivingBehavior",
        "data:telemetry:vehicle:wipingBlades",
        "data:telemetry:vehicle:alarm",
        "data:position",
        "data:trip",
        "data:alert",
        "data:collision",
    ],
    typing.Any,
]
