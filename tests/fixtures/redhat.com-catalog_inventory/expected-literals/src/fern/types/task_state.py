

import typing

TaskState = typing.Union[typing.Literal["pending", "queued", "running", "timedout", "completed"], typing.Any]
