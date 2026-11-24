

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NullableColor(enum.StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def visit(
        self,
        red: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        blue: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NullableColor.RED:
            return red()
        if self is NullableColor.GREEN:
            return green()
        if self is NullableColor.BLUE:
            return blue()
