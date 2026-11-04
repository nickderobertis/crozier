

import typing

PluginStatusPhase = typing.Union[
    typing.Literal[
        "PENDING", "STARTING", "CREATED", "DISABLING", "DISABLED", "RESOLVED", "STARTED", "STOPPED", "FAILED", "UNKNOWN"
    ],
    typing.Any,
]
