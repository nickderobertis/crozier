

import typing

WritableDeviceWithConfigContextStatus = typing.Union[
    typing.Literal["offline", "active", "planned", "staged", "failed", "inventory", "decommissioning"], typing.Any
]
