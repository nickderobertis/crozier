

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MessageType(enum.StrEnum):
    SYSTEM_MESSAGE = "system_message"
    USER_MESSAGE = "user_message"
    ASSISTANT_MESSAGE = "assistant_message"
    REASONING_MESSAGE = "reasoning_message"
    HIDDEN_REASONING_MESSAGE = "hidden_reasoning_message"
    TOOL_CALL_MESSAGE = "tool_call_message"
    TOOL_RETURN_MESSAGE = "tool_return_message"
    APPROVAL_REQUEST_MESSAGE = "approval_request_message"
    APPROVAL_RESPONSE_MESSAGE = "approval_response_message"

    def visit(
        self,
        system_message: typing.Callable[[], T_Result],
        user_message: typing.Callable[[], T_Result],
        assistant_message: typing.Callable[[], T_Result],
        reasoning_message: typing.Callable[[], T_Result],
        hidden_reasoning_message: typing.Callable[[], T_Result],
        tool_call_message: typing.Callable[[], T_Result],
        tool_return_message: typing.Callable[[], T_Result],
        approval_request_message: typing.Callable[[], T_Result],
        approval_response_message: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MessageType.SYSTEM_MESSAGE:
            return system_message()
        if self is MessageType.USER_MESSAGE:
            return user_message()
        if self is MessageType.ASSISTANT_MESSAGE:
            return assistant_message()
        if self is MessageType.REASONING_MESSAGE:
            return reasoning_message()
        if self is MessageType.HIDDEN_REASONING_MESSAGE:
            return hidden_reasoning_message()
        if self is MessageType.TOOL_CALL_MESSAGE:
            return tool_call_message()
        if self is MessageType.TOOL_RETURN_MESSAGE:
            return tool_return_message()
        if self is MessageType.APPROVAL_REQUEST_MESSAGE:
            return approval_request_message()
        if self is MessageType.APPROVAL_RESPONSE_MESSAGE:
            return approval_response_message()
