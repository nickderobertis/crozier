

import typing

JobGetDetailsResponseStatus = typing.Union[
    typing.Literal[
        "success",
        "running",
        "not_run",
        "failed",
        "retried",
        "queued",
        "not_running",
        "infrastructure_fail",
        "timedout",
        "on_hold",
        "terminated-unknown",
        "blocked",
        "canceled",
        "unauthorized",
    ],
    typing.Any,
]
