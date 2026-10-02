

import typing

MessageStatus = typing.Union[
    typing.Literal[
        "accepted",
        "scheduled",
        "canceled",
        "queued",
        "sending",
        "sent",
        "failed",
        "delivered",
        "undelivered",
        "receiving",
        "received",
        "read",
    ],
    typing.Any,
]
