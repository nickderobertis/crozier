

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelOpenMethod(enum.StrEnum):
    OPEN = "open"

    def visit(self, open: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelOpenMethod.OPEN:
            return open()
