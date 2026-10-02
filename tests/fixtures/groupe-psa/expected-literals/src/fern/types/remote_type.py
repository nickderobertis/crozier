

import typing

RemoteType = typing.Union[
    typing.Literal[
        "ThermalPreconditioning",
        "ElectricBatteryChargingRequest",
        "Horn",
        "Doors",
        "Lights",
        "Immobilization",
        "Stolen",
        "WakeUp",
        "Navigation",
    ],
    typing.Any,
]
