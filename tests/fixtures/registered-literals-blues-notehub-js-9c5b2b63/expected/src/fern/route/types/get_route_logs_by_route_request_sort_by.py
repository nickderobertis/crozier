

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRouteLogsByRouteRequestSortBy(enum.StrEnum):
    DATE = "date"
    EVENT = "event"

    def visit(self, date: typing.Callable[[], T_Result], event: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRouteLogsByRouteRequestSortBy.DATE:
            return date()
        if self is GetRouteLogsByRouteRequestSortBy.EVENT:
            return event()
