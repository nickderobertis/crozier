

import typing

PilotWorkerStatusStatus = typing.Union[
    typing.Literal["starting", "healthy", "stale", "degraded", "stopped"], typing.Any
]
