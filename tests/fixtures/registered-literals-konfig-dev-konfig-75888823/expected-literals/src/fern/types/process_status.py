

import typing

ProcessStatus = typing.Union[
    typing.Literal["starting", "running", "draining", "stopping", "stopped", "failed"], typing.Any
]
