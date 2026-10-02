

import typing

WebhookEventsItem = typing.Union[
    typing.Literal["post", "comment", "chat_message", "member_join", "member_leave"], typing.Any
]
