

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SlackBearerNotificationMessageType(enum.StrEnum):
    """
    text or blocks
    """

    TEXT = "text"
    BLOCKS = "blocks"

    def visit(self, text: typing.Callable[[], T_Result], blocks: typing.Callable[[], T_Result]) -> T_Result:
        if self is SlackBearerNotificationMessageType.TEXT:
            return text()
        if self is SlackBearerNotificationMessageType.BLOCKS:
            return blocks()
