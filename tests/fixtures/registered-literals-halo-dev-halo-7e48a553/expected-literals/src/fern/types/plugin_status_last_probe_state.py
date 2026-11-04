

import typing

PluginStatusLastProbeState = typing.Union[
    typing.Literal["CREATED", "DISABLED", "RESOLVED", "STARTED", "STOPPED", "FAILED", "UNLOADED"], typing.Any
]
