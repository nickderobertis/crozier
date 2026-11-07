

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetRouteLogsByRouteRequestRoutingStatusItem(enum.StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"

    def visit(self, success: typing.Callable[[], T_Result], failure: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetRouteLogsByRouteRequestRoutingStatusItem.SUCCESS:
            return success()
        if self is GetRouteLogsByRouteRequestRoutingStatusItem.FAILURE:
            return failure()
