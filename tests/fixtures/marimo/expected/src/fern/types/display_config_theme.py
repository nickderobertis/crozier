

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DisplayConfigTheme(enum.StrEnum):
    DARK = "dark"
    LIGHT = "light"
    SYSTEM = "system"

    def visit(
        self,
        dark: typing.Callable[[], T_Result],
        light: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DisplayConfigTheme.DARK:
            return dark()
        if self is DisplayConfigTheme.LIGHT:
            return light()
        if self is DisplayConfigTheme.SYSTEM:
            return system()
