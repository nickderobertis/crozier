

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CaseTrackScheduleType(enum.StrEnum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

    def visit(
        self,
        daily: typing.Callable[[], T_Result],
        weekly: typing.Callable[[], T_Result],
        monthly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CaseTrackScheduleType.DAILY:
            return daily()
        if self is CaseTrackScheduleType.WEEKLY:
            return weekly()
        if self is CaseTrackScheduleType.MONTHLY:
            return monthly()
