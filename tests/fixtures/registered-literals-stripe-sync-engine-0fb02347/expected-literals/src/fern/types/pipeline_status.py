

import typing

PipelineStatus = typing.Union[typing.Literal["setup", "backfill", "ready", "paused", "teardown", "error"], typing.Any]
