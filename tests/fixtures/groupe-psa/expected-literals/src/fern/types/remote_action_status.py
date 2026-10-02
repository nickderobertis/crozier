

import typing

RemoteActionStatus = typing.Union[
    typing.Literal[
        "Accepted",
        "Failed",
        "Success",
        "AlreadyDone",
        "WakingUpVehicle",
        "CheckingVehicle",
        "SentToVehicle",
        "VehicleBatteryChargeTooLow",
        "TooManyWakeUpsOverMonth",
    ],
    typing.Any,
]
