

import typing

DoorsStateBaseLockedStatesItem = typing.Union[
    typing.Literal[
        "Unlocked",
        "Locked",
        "SuperLocked",
        "DriverDoorUnlocked",
        "CabinDoorsUnlocked",
        "CargoDoorsLocked",
        "CargoDoorsUnlocked",
        "RearDoorsUnlocked",
        "RearDoorsLocked",
        "TrunkLocked",
        "TrunkUnLocked",
    ],
    typing.Any,
]
