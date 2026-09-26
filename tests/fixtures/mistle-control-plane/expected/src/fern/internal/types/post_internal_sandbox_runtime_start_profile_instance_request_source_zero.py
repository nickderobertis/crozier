

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero(enum.StrEnum):
    DASHBOARD = "dashboard"

    def visit(self, dashboard: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeStartProfileInstanceRequestSourceZero.DASHBOARD:
            return dashboard()
