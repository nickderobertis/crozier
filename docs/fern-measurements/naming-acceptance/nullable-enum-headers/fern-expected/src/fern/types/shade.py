

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Shade(enum.StrEnum):
    LIGHT = "light"
    DARK = "dark"

    def visit(self, light: typing.Callable[[], T_Result], dark: typing.Callable[[], T_Result]) -> T_Result:
        if self is Shade.LIGHT:
            return light()
        if self is Shade.DARK:
            return dark()
