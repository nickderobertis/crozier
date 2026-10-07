

import typing

PreconditioningAirConditioningFailureCause = typing.Union[
    typing.Literal[
        "Defect",
        "DoorOpened",
        "LowBattery",
        "LowFuelLevel",
        "TooManyUnusedProg",
        "WindowsRoofOpened",
        "HoodOpened",
        "NotParked",
        "OtherFailures",
    ],
    typing.Any,
]
