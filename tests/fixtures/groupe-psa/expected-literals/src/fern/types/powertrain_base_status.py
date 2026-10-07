

import typing

PowertrainBaseStatus = typing.Union[
    typing.Literal["NotRunning", "Starting", "Running", "Stopping", "Stopped"], typing.Any
]
