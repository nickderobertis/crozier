

import typing

CircuitStatusValue = typing.Union[
    typing.Literal["planned", "provisioning", "active", "offline", "deprovisioning", "decommissioned"], typing.Any
]
