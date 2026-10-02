

import typing

ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageIncludeReturnMessageTypesItem = typing.Union[
    typing.Literal[
        "system_message",
        "user_message",
        "assistant_message",
        "reasoning_message",
        "hidden_reasoning_message",
        "tool_call_message",
        "tool_return_message",
        "approval_request_message",
        "approval_response_message",
    ],
    typing.Any,
]
