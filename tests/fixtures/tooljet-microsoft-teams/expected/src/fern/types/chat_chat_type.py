

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChatChatType(enum.StrEnum):
    """
    Type of chat
    """

    ONE_ON_ONE = "oneOnOne"
    GROUP = "group"
    MEETING = "meeting"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

    def visit(
        self,
        one_on_one: typing.Callable[[], T_Result],
        group: typing.Callable[[], T_Result],
        meeting: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChatChatType.ONE_ON_ONE:
            return one_on_one()
        if self is ChatChatType.GROUP:
            return group()
        if self is ChatChatType.MEETING:
            return meeting()
        if self is ChatChatType.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
