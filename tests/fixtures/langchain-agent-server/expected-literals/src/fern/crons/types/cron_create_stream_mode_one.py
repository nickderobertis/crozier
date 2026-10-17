

import typing

CronCreateStreamModeOne = typing.Union[
    typing.Literal[
        "values", "messages", "messages-tuple", "tasks", "checkpoints", "updates", "events", "debug", "custom"
    ],
    typing.Any,
]
