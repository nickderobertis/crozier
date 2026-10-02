

import typing

DeviceTypeAirflowLabel = typing.Union[
    typing.Literal[
        "Front to rear", "Rear to front", "Left to right", "Right to left", "Side to rear", "Passive", "Mixed"
    ],
    typing.Any,
]
