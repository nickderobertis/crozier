

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdatePreferencesRequestTheme(enum.StrEnum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"

    def visit(
        self,
        light: typing.Callable[[], T_Result],
        dark: typing.Callable[[], T_Result],
        system: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdatePreferencesRequestTheme.LIGHT:
            return light()
        if self is UpdatePreferencesRequestTheme.DARK:
            return dark()
        if self is UpdatePreferencesRequestTheme.SYSTEM:
            return system()
