

import typing

PermissionResourceType = typing.Union[
    typing.Literal["agent", "schedule", "session", "tenant", "sandbox_environment"], typing.Any
]
