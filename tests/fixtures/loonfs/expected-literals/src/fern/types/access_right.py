

import typing

AccessRight = typing.Union[
    typing.Literal["read", "history", "write", "create", "remove", "share", "manage", "admin"], typing.Any
]
