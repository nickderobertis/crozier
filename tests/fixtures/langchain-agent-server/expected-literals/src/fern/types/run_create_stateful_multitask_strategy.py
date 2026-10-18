

import typing

RunCreateStatefulMultitaskStrategy = typing.Union[
    typing.Literal["reject", "rollback", "interrupt", "enqueue"], typing.Any
]
