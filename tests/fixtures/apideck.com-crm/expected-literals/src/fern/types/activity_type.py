

import typing

ActivityType = typing.Union[
    typing.Literal["call", "meeting", "email", "note", "task", "deadline", "send-letter", "send-quote", "other"],
    typing.Any,
]
