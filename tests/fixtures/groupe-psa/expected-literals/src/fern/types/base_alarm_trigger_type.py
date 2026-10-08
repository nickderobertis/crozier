

import typing

BaseAlarmTriggerType = typing.Union[
    typing.Literal[
        "NoBreakIn",
        "FrontRightDoorBreakIn",
        "FrontLeftDoorBreakIn",
        "RearRightFrontDoorBreakIn",
        "RearLeftFrontDoorBreakIn",
        "HoodDoorBreakIn",
        "TrunkDoorBreakIn",
        "BackliteDoorBreakIn",
        "RoofBreakIn",
        "VolumetricBreakIn",
        "VehicleLifting",
        "ElectricalsystemBreakIn",
        "KeyLearning",
        "UnauthenticatedStartup",
    ],
    typing.Any,
]
