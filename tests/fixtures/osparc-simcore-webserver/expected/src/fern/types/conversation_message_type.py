

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationMessageType(enum.StrEnum):
    MESSAGE = "MESSAGE"
    NOTIFICATION = "NOTIFICATION"

    def visit(self, message: typing.Callable[[], T_Result], notification: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConversationMessageType.MESSAGE:
            return message()
        if self is ConversationMessageType.NOTIFICATION:
            return notification()
