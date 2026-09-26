

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class MonitoringProjectsDashboardsCreateRequestXgafv(enum.StrEnum):
    ONE = "1"
    TWO = "2"

    def visit(self, one: typing.Callable[[], T_Result], two: typing.Callable[[], T_Result]) -> T_Result:
        if self is MonitoringProjectsDashboardsCreateRequestXgafv.ONE:
            return one()
        if self is MonitoringProjectsDashboardsCreateRequestXgafv.TWO:
            return two()
