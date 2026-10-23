

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyDisplayOption(enum.StrEnum):
    """
    Display options for the survey
    """

    DISPLAY_ONCE = "displayOnce"
    DISPLAY_MULTIPLE = "displayMultiple"
    DISPLAY_SOME = "displaySome"
    RESPOND_MULTIPLE = "respondMultiple"

    def visit(
        self,
        display_once: typing.Callable[[], T_Result],
        display_multiple: typing.Callable[[], T_Result],
        display_some: typing.Callable[[], T_Result],
        respond_multiple: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyDisplayOption.DISPLAY_ONCE:
            return display_once()
        if self is SurveyDisplayOption.DISPLAY_MULTIPLE:
            return display_multiple()
        if self is SurveyDisplayOption.DISPLAY_SOME:
            return display_some()
        if self is SurveyDisplayOption.RESPOND_MULTIPLE:
            return respond_multiple()
