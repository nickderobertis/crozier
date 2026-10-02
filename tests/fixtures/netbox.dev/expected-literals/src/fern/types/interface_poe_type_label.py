

import typing

InterfacePoeTypeLabel = typing.Union[
    typing.Literal[
        "802.3af (Type 1)",
        "802.3at (Type 2)",
        "802.3az (Type 2)",
        "802.3bt (Type 3)",
        "802.3bt (Type 4)",
        "Passive 24V (2-pair)",
        "Passive 24V (4-pair)",
        "Passive 48V (2-pair)",
        "Passive 48V (4-pair)",
    ],
    typing.Any,
]
