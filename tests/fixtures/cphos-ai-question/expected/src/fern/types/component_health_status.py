

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ComponentHealthStatus(enum.StrEnum):
    """
    组件健康状态。
    """

    OK = "ok"
    ERROR = "error"

    def visit(self, ok: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is ComponentHealthStatus.OK:
            return ok()
        if self is ComponentHealthStatus.ERROR:
            return error()
