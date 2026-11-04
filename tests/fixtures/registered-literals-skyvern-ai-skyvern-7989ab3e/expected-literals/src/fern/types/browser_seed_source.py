

import typing

BrowserSeedSource = typing.Union[
    typing.Literal["override", "picked", "own_memory", "credential", "fresh", "degraded_fresh"], typing.Any
]
