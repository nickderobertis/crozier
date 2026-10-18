

import typing

ThreadCronCreateMultitaskStrategy = typing.Union[
    typing.Literal["reject", "rollback", "interrupt", "enqueue"], typing.Any
]
