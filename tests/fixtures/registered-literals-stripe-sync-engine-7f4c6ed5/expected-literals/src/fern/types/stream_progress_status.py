

import typing

StreamProgressStatus = typing.Union[
    typing.Literal["not_started", "started", "completed", "skipped", "errored"], typing.Any
]
