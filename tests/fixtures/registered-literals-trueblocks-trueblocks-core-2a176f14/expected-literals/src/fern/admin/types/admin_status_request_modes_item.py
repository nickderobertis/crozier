

import typing

AdminStatusRequestModesItem = typing.Union[
    typing.Literal[
        "index",
        "blooms",
        "blocks",
        "transactions",
        "traces",
        "logs",
        "statements",
        "results",
        "state",
        "tokens",
        "monitors",
        "names",
        "abis",
        "slurps",
        "staging",
        "unripe",
        "maps",
        "some",
        "all",
    ],
    typing.Any,
]
