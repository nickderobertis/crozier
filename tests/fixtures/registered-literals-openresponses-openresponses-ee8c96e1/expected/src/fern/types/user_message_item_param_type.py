

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserMessageItemParamType(enum.StrEnum):
    """
    The item type. Always `message`.
    """

    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserMessageItemParamType.MESSAGE:
            return message()
