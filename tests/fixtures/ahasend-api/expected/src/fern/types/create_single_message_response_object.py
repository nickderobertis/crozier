

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSingleMessageResponseObject(enum.StrEnum):
    """
    Object type identifier
    """

    MESSAGE = "message"

    def visit(self, message: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSingleMessageResponseObject.MESSAGE:
            return message()
