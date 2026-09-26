

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoCodeEditorDataTheme(enum.StrEnum):
    LIGHT = "light"
    DARK = "dark"

    def visit(self, light: typing.Callable[[], T_Result], dark: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoCodeEditorDataTheme.LIGHT:
            return light()
        if self is MarimoCodeEditorDataTheme.DARK:
            return dark()
