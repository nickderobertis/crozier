

import typing

WritableLocationStatus = typing.Union[
    typing.Literal["planned", "staging", "active", "decommissioning", "retired"], typing.Any
]
