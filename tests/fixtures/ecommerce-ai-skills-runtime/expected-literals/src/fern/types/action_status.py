

import typing

ActionStatus = typing.Union[
    typing.Literal["requested", "approved", "executing", "executed", "failed", "rejected"], typing.Any
]
