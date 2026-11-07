

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SystemMessageItemParamType(enum.StrEnum):
    """
    The item type. Always `message`.
    """

    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is SystemMessageItemParamType.MESSAGE:
            return message()
