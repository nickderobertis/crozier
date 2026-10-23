

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyWorkspaceOverwritesPlacement(enum.StrEnum):
    BOTTOM_LEFT = "bottomLeft"
    BOTTOM_RIGHT = "bottomRight"
    TOP_LEFT = "topLeft"
    TOP_RIGHT = "topRight"
    CENTER = "center"

    def visit(
        self,
        bottom_left: typing.Callable[[], T_Result],
        bottom_right: typing.Callable[[], T_Result],
        top_left: typing.Callable[[], T_Result],
        top_right: typing.Callable[[], T_Result],
        center: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyWorkspaceOverwritesPlacement.BOTTOM_LEFT:
            return bottom_left()
        if self is SurveyWorkspaceOverwritesPlacement.BOTTOM_RIGHT:
            return bottom_right()
        if self is SurveyWorkspaceOverwritesPlacement.TOP_LEFT:
            return top_left()
        if self is SurveyWorkspaceOverwritesPlacement.TOP_RIGHT:
            return top_right()
        if self is SurveyWorkspaceOverwritesPlacement.CENTER:
            return center()
