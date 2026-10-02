

import typing

ClusterStatusValue = typing.Union[
    typing.Literal["planned", "staging", "active", "decommissioning", "offline"], typing.Any
]
