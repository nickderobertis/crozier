

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TextMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `text` in this field
    """

    TEXT = "text"

    def visit(self, text: typing.Callable[[], T_Result]) -> T_Result:
        if self is TextMessageType.TEXT:
            return text()
