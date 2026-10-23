

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyStatus(enum.StrEnum):
    """
    The status of the survey
    """

    DRAFT = "draft"
    IN_PROGRESS = "inProgress"
    PAUSED = "paused"
    COMPLETED = "completed"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyStatus.DRAFT:
            return draft()
        if self is SurveyStatus.IN_PROGRESS:
            return in_progress()
        if self is SurveyStatus.PAUSED:
            return paused()
        if self is SurveyStatus.COMPLETED:
            return completed()
