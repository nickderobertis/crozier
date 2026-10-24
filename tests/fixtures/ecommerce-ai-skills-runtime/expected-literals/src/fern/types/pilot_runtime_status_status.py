

import typing

PilotRuntimeStatusStatus = typing.Union[
    typing.Literal["starting", "healthy", "stale", "degraded", "stopping", "stopped", "superseded"], typing.Any
]
