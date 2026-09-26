

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoTableDataTextJustifyColumnsValue(enum.StrEnum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

    def visit(
        self,
        left: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MarimoTableDataTextJustifyColumnsValue.LEFT:
            return left()
        if self is MarimoTableDataTextJustifyColumnsValue.CENTER:
            return center()
        if self is MarimoTableDataTextJustifyColumnsValue.RIGHT:
            return right()
