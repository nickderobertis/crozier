

import typing

DeviceStatusValue = typing.Union[
    typing.Literal["offline", "active", "planned", "staged", "failed", "inventory", "decommissioning"], typing.Any
]
