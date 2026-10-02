

import typing

DeviceTypeAirflowValue = typing.Union[
    typing.Literal[
        "front-to-rear", "rear-to-front", "left-to-right", "right-to-left", "side-to-rear", "passive", "mixed"
    ],
    typing.Any,
]
