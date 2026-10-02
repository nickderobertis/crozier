

import typing

TransactionSource = typing.Union[
    typing.Literal["cell-manager", "code-mode", "file-watch", "frontend", "kernel"], typing.Any
]
