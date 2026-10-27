

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatMessageMessageType(enum.StrEnum):
    MESSAGE = "message"
    CHAT_EVENT = "chatEvent"
    TYPING = "typing"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"
    SYSTEM_EVENT_MESSAGE = "systemEventMessage"

    def visit(
        self,
        message: typing.Callable[[], T_Result],
        chat_event: typing.Callable[[], T_Result],
        typing: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
        system_event_message: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatMessageMessageType.MESSAGE:
            return message()
        if self is ChatMessageMessageType.CHAT_EVENT:
            return chat_event()
        if self is ChatMessageMessageType.TYPING:
            return typing()
        if self is ChatMessageMessageType.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
        if self is ChatMessageMessageType.SYSTEM_EVENT_MESSAGE:
            return system_event_message()
