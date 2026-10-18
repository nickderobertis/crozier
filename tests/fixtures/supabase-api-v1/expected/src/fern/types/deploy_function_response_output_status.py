

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DeployFunctionResponseOutputStatus(enum.StrEnum):
    ACTIVE = "ACTIVE"
    REMOVED = "REMOVED"
    THROTTLED = "THROTTLED"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        removed: typing.Callable[[], T_Result],
        throttled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeployFunctionResponseOutputStatus.ACTIVE:
            return active()
        if self is DeployFunctionResponseOutputStatus.REMOVED:
            return removed()
        if self is DeployFunctionResponseOutputStatus.THROTTLED:
            return throttled()
