

import typing

DrivingBehaviorBaseMode = typing.Union[
    typing.Literal[
        "Normal",
        "Sport",
        "Comfort",
        "Eco",
        "Sand",
        "Mud",
        "Snow",
        "ZEV",
        "Hybrid",
        "ZEVEco",
        "HybridEco",
        "EcoPlus",
        "eAWD",
        "4AWD",
        "ReinforcedLoad",
    ],
    typing.Any,
]
