

import typing

WritableVirtualMachineWithConfigContextStatus = typing.Union[
    typing.Literal["offline", "active", "planned", "staged", "failed", "decommissioning"], typing.Any
]
