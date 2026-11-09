

import typing

EventType = typing.Union[
    typing.Literal[
        "miner",
        "foundation",
        "siafundClaim",
        "v1Transaction",
        "v1ContractResolution",
        "v2Transaction",
        "v2ContractResolution",
    ],
    typing.Any,
]
