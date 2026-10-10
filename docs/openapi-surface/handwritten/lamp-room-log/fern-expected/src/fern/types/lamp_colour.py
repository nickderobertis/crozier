

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LampColour(enum.StrEnum):
    WHITE = "white"
    RED = "red"
    GREEN = "green"

    def visit(
        self,
        white: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LampColour.WHITE:
            return white()
        if self is LampColour.RED:
            return red()
        if self is LampColour.GREEN:
            return green()
