

import typing

WritableClusterStatus = typing.Union[
    typing.Literal["planned", "staging", "active", "decommissioning", "offline"], typing.Any
]
