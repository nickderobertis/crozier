

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoNavMenuDataOrientation(enum.StrEnum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

    def visit(self, horizontal: typing.Callable[[], T_Result], vertical: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoNavMenuDataOrientation.HORIZONTAL:
            return horizontal()
        if self is MarimoNavMenuDataOrientation.VERTICAL:
            return vertical()
