

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelingOperationActionPartTintTintModeOne(enum.StrEnum):
    SCREEN = "screen"

    def visit(self, screen: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelingOperationActionPartTintTintModeOne.SCREEN:
            return screen()
