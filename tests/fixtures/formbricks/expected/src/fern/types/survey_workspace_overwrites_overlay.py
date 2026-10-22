

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyWorkspaceOverwritesOverlay(enum.StrEnum):
    NONE = "none"
    LIGHT = "light"
    DARK = "dark"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        light: typing.Callable[[], T_Result],
        dark: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyWorkspaceOverwritesOverlay.NONE:
            return none()
        if self is SurveyWorkspaceOverwritesOverlay.LIGHT:
            return light()
        if self is SurveyWorkspaceOverwritesOverlay.DARK:
            return dark()
