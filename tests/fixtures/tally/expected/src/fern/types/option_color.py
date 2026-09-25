

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OptionColor(enum.StrEnum):
    """
    Color name for this option when colorCodeOptions is enabled.
    """

    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    BLUE = "blue"
    PURPLE = "purple"
    PINK = "pink"
    GRAY = "gray"

    def visit(
        self,
        red: typing.Callable[[], T_Result],
        orange: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        blue: typing.Callable[[], T_Result],
        purple: typing.Callable[[], T_Result],
        pink: typing.Callable[[], T_Result],
        gray: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OptionColor.RED:
            return red()
        if self is OptionColor.ORANGE:
            return orange()
        if self is OptionColor.YELLOW:
            return yellow()
        if self is OptionColor.GREEN:
            return green()
        if self is OptionColor.BLUE:
            return blue()
        if self is OptionColor.PURPLE:
            return purple()
        if self is OptionColor.PINK:
            return pink()
        if self is OptionColor.GRAY:
            return gray()
