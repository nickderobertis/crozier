

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRouteLogsUsageRequestAggregate(enum.StrEnum):
    ROUTE = "route"
    PROJECT = "project"

    def visit(self, route: typing.Callable[[], T_Result], project: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRouteLogsUsageRequestAggregate.ROUTE:
            return route()
        if self is GetRouteLogsUsageRequestAggregate.PROJECT:
            return project()
