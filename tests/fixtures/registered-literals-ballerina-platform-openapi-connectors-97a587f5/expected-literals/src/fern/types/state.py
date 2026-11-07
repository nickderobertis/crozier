

import typing

State = typing.Union[typing.Literal["notRunning", "running", "succeeded", "canceled", "failed", "deleted"], typing.Any]
