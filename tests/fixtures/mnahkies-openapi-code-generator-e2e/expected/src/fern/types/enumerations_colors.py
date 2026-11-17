

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EnumerationsColors(enum.StrEnum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"

    def visit(
        self,
        red: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        blue: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EnumerationsColors.RED:
            return red()
        if self is EnumerationsColors.GREEN:
            return green()
        if self is EnumerationsColors.BLUE:
            return blue()
