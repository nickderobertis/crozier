

import typing

RemoteFailedEventStatus = typing.Union[
    typing.Literal[
        "GeneralError",
        "VehicleError",
        "WrongCommand",
        "VehicleConnectionTimeout",
        "MissingRights",
        "NotPossibleDueToVehicleBatteryLevel",
        "NotPossibleDueToVehiclePrivacyLevel",
        "TooManyWakeUpsOverMonth",
        "TooManyRequestInShortTime",
        "SameActionInProgress",
        "NotPossibleDueToVehicleStolenState",
        "VehicleInUse",
        "TooManyRequestSent",
        "DoorsOpen",
        "VehicleErrorOrCidInside",
        "CidInside",
        "ExternalChargingSystemError",
        "VehicleChargingSystemError",
        "VehicleIsNotLocked",
        "CanceledByDriver",
    ],
    typing.Any,
]
