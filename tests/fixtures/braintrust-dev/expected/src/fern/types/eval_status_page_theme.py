

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EvalStatusPageTheme(enum.StrEnum):
    """
    The theme for the page
    """

    LIGHT = "light"
    DARK = "dark"

    def visit(self, light: typing.Callable[[], T_Result], dark: typing.Callable[[], T_Result]) -> T_Result:
        if self is EvalStatusPageTheme.LIGHT:
            return light()
        if self is EvalStatusPageTheme.DARK:
            return dark()
