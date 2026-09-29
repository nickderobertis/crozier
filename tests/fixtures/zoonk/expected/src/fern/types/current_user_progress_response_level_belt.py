

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CurrentUserProgressResponseLevelBelt(enum.StrEnum):
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
        if self is CurrentUserProgressResponseLevelBelt.WHITE:
            return white()
        if self is CurrentUserProgressResponseLevelBelt.YELLOW:
            return yellow()
        if self is CurrentUserProgressResponseLevelBelt.ORANGE:
            return orange()
        if self is CurrentUserProgressResponseLevelBelt.GREEN:
            return green()
        if self is CurrentUserProgressResponseLevelBelt.BLUE:
            return blue()
        if self is CurrentUserProgressResponseLevelBelt.PURPLE:
            return purple()
        if self is CurrentUserProgressResponseLevelBelt.BROWN:
            return brown()
        if self is CurrentUserProgressResponseLevelBelt.RED:
            return red()
        if self is CurrentUserProgressResponseLevelBelt.GRAY:
            return gray()
        if self is CurrentUserProgressResponseLevelBelt.BLACK:
            return black()
