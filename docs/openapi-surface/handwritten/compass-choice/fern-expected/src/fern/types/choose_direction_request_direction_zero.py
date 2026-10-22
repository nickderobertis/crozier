

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChooseDirectionRequestDirectionZero(enum.StrEnum):
    NORTH = "north"

    def visit(self, north: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChooseDirectionRequestDirectionZero.NORTH:
            return north()
