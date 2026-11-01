

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BalloonColor(enum.StrEnum):
    BLUE = "blue"
    GREEN = "green"
    RED = "red"

    def visit(
        self,
        blue: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BalloonColor.BLUE:
            return blue()
        if self is BalloonColor.GREEN:
            return green()
        if self is BalloonColor.RED:
            return red()
