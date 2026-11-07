

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeveloperMessageItemParamType(enum.StrEnum):
    """
    The item type. Always `message`.
    """

    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeveloperMessageItemParamType.MESSAGE:
            return message()
