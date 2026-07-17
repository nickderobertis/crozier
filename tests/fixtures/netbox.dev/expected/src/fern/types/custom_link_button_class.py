

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CustomLinkButtonClass(enum.StrEnum):
    """
    The class of the first link in a group will be used for the dropdown button
    """

    OUTLINE_DARK = "outline-dark"
    BLUE = "blue"
    INDIGO = "indigo"
    PURPLE = "purple"
    PINK = "pink"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GREEN = "green"
    TEAL = "teal"
    CYAN = "cyan"
    GRAY = "gray"
    BLACK = "black"
    WHITE = "white"
    GHOST_DARK = "ghost-dark"

    def visit(
        self,
        outline_dark: typing.Callable[[], T_Result],
        blue: typing.Callable[[], T_Result],
        indigo: typing.Callable[[], T_Result],
        purple: typing.Callable[[], T_Result],
        pink: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
        orange: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        green: typing.Callable[[], T_Result],
        teal: typing.Callable[[], T_Result],
        cyan: typing.Callable[[], T_Result],
        gray: typing.Callable[[], T_Result],
        black: typing.Callable[[], T_Result],
        white: typing.Callable[[], T_Result],
        ghost_dark: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CustomLinkButtonClass.OUTLINE_DARK:
            return outline_dark()
        if self is CustomLinkButtonClass.BLUE:
            return blue()
        if self is CustomLinkButtonClass.INDIGO:
            return indigo()
        if self is CustomLinkButtonClass.PURPLE:
            return purple()
        if self is CustomLinkButtonClass.PINK:
            return pink()
        if self is CustomLinkButtonClass.RED:
            return red()
        if self is CustomLinkButtonClass.ORANGE:
            return orange()
        if self is CustomLinkButtonClass.YELLOW:
            return yellow()
        if self is CustomLinkButtonClass.GREEN:
            return green()
        if self is CustomLinkButtonClass.TEAL:
            return teal()
        if self is CustomLinkButtonClass.CYAN:
            return cyan()
        if self is CustomLinkButtonClass.GRAY:
            return gray()
        if self is CustomLinkButtonClass.BLACK:
            return black()
        if self is CustomLinkButtonClass.WHITE:
            return white()
        if self is CustomLinkButtonClass.GHOST_DARK:
            return ghost_dark()
