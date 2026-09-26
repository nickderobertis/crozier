

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListReportsRequestReportFrequency(enum.StrEnum):
    ONE_TIME = "one_time"
    SCHEDULED = "scheduled"

    def visit(self, one_time: typing.Callable[[], T_Result], scheduled: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListReportsRequestReportFrequency.ONE_TIME:
            return one_time()
        if self is ListReportsRequestReportFrequency.SCHEDULED:
            return scheduled()
