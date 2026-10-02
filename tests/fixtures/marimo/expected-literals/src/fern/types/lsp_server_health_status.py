

import typing

LspServerHealthStatus = typing.Union[
    typing.Literal["crashed", "running", "starting", "stopped", "unresponsive"], typing.Any
]
