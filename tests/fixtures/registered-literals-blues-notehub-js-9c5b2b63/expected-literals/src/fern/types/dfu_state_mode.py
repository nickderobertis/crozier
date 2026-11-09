

import typing

DfuStateMode = typing.Union[
    typing.Literal["idle", "error", "downloading", "sideloading", "ready", "ready-retry", "updating", "completed"],
    typing.Any,
]
