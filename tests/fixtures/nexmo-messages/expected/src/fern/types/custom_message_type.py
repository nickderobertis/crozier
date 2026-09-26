

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomMessageType(enum.StrEnum):
    """
    The type of message to send. You must provide `custom` in this field
    """

    CUSTOM = "custom"

    def visit(self, custom: typing.Callable[[], T_Result]) -> T_Result:
        if self is CustomMessageType.CUSTOM:
            return custom()
