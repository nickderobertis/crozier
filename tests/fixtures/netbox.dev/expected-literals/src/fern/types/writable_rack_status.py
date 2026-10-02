

import typing

WritableRackStatus = typing.Union[
    typing.Literal["reserved", "available", "planned", "active", "deprecated"], typing.Any
]
