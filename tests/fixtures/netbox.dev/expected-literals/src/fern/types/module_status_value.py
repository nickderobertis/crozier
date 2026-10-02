

import typing

ModuleStatusValue = typing.Union[
    typing.Literal["offline", "active", "planned", "staged", "failed", "decommissioning"], typing.Any
]
