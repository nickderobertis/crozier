

import typing

PostWebhooksRequestEvent = typing.Union[
    typing.Literal[
        "conversation_message",
        "conversation_seen",
        "group_update",
        "group_message",
        "group_seen",
        "user_online",
        "user_update",
    ],
    typing.Any,
]
