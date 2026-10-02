

import typing

WritableCircuitStatus = typing.Union[
    typing.Literal["planned", "provisioning", "active", "offline", "deprovisioning", "decommissioned"], typing.Any
]
