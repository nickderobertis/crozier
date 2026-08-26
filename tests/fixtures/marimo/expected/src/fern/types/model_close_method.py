

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelCloseMethod(enum.StrEnum):
    CLOSE = "close"

    def visit(self, close: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelCloseMethod.CLOSE:
            return close()
