

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SlackWebHookNotificationMessageType(enum.StrEnum):
    """
    text or blocks
    """

    TEXT = "text"
    BLOCKS = "blocks"

    def visit(self, text: typing.Callable[[], T_Result], blocks: typing.Callable[[], T_Result]) -> T_Result:
        if self is SlackWebHookNotificationMessageType.TEXT:
            return text()
        if self is SlackWebHookNotificationMessageType.BLOCKS:
            return blocks()
