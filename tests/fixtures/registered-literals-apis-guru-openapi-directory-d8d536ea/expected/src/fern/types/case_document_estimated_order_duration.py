

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseDocumentEstimatedOrderDuration(enum.StrEnum):
    """
    Estimated duration of a Order.
    """

    ESTIMATE_UNAVAILABLE = "estimateUnavailable"
    WITHIN_MINUTES = "withinMinutes"
    WITHIN_HOURS = "withinHours"
    WITHIN_DAYS = "withinDays"
    WITHIN_WEEKS = "withinWeeks"

    def visit(
        self,
        estimate_unavailable: typing.Callable[[], T_Result],
        within_minutes: typing.Callable[[], T_Result],
        within_hours: typing.Callable[[], T_Result],
        within_days: typing.Callable[[], T_Result],
        within_weeks: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseDocumentEstimatedOrderDuration.ESTIMATE_UNAVAILABLE:
            return estimate_unavailable()
        if self is CaseDocumentEstimatedOrderDuration.WITHIN_MINUTES:
            return within_minutes()
        if self is CaseDocumentEstimatedOrderDuration.WITHIN_HOURS:
            return within_hours()
        if self is CaseDocumentEstimatedOrderDuration.WITHIN_DAYS:
            return within_days()
        if self is CaseDocumentEstimatedOrderDuration.WITHIN_WEEKS:
            return within_weeks()
