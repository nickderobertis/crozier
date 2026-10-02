

import typing

ServiceState = typing.Union[
    typing.Literal["failed", "pending", "pulling", "starting", "running", "stopping", "complete", "idle"], typing.Any
]
