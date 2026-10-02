

import typing

StreamingChannelZero = typing.Union[
    typing.Literal["values", "updates", "messages", "tools", "lifecycle", "input", "checkpoints", "tasks", "custom"],
    typing.Any,
]
