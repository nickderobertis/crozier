

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsDashboardsPatchRequestXgafv(enum.StrEnum):
    ONE = "1"
    TWO = "2"

    def visit(self, one: typing.Callable[[], T_Result], two: typing.Callable[[], T_Result]) -> T_Result:
        if self is MonitoringProjectsDashboardsPatchRequestXgafv.ONE:
            return one()
        if self is MonitoringProjectsDashboardsPatchRequestXgafv.TWO:
            return two()
