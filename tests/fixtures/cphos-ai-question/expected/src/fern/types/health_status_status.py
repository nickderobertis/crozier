

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HealthStatusStatus(enum.StrEnum):
    """
    整体状态：所有组件正常为 ok，任一组件异常为 degraded。
    """

    OK = "ok"
    DEGRADED = "degraded"

    def visit(self, ok: typing.Callable[[], T_Result], degraded: typing.Callable[[], T_Result]) -> T_Result:
        if self is HealthStatusStatus.OK:
            return ok()
        if self is HealthStatusStatus.DEGRADED:
            return degraded()
