

import typing

PluginRequirementKind = typing.Union[
    typing.Literal["platform", "hardware", "region", "network", "provider", "player"], typing.Any
]
