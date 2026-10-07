

import typing

EngineBaseGmpStatus = typing.Union[
    typing.Literal["NotRunning", "Starting", "Running", "Stopping", "Stopped"], typing.Any
]
