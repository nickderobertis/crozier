

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserLevelResponseLevelBelt(enum.StrEnum):
    WHITE = "white"
    YELLOW = "yellow"
    ORANGE = "orange"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    BROWN = "brown"
    RED = "red"
    GRAY = "gray"
    BLACK = "black"

    def visit(
        self,
        white: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        orange: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        blue: typing.Callable[[], T_Result],
        purple: typing.Callable[[], T_Result],
        brown: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
        gray: typing.Callable[[], T_Result],
        black: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CurrentUserLevelResponseLevelBelt.WHITE:
            return white()
        if self is CurrentUserLevelResponseLevelBelt.YELLOW:
            return yellow()
        if self is CurrentUserLevelResponseLevelBelt.ORANGE:
            return orange()
        if self is CurrentUserLevelResponseLevelBelt.GREEN:
            return green()
        if self is CurrentUserLevelResponseLevelBelt.BLUE:
            return blue()
        if self is CurrentUserLevelResponseLevelBelt.PURPLE:
            return purple()
        if self is CurrentUserLevelResponseLevelBelt.BROWN:
            return brown()
        if self is CurrentUserLevelResponseLevelBelt.RED:
            return red()
        if self is CurrentUserLevelResponseLevelBelt.GRAY:
            return gray()
        if self is CurrentUserLevelResponseLevelBelt.BLACK:
            return black()
