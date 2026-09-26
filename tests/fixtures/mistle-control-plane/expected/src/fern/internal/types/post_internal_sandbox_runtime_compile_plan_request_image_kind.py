

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanRequestImageKind(enum.StrEnum):
    BASE = "base"
    SNAPSHOT = "snapshot"

    def visit(self, base: typing.Callable[[], T_Result], snapshot: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostInternalSandboxRuntimeCompilePlanRequestImageKind.BASE:
            return base()
        if self is PostInternalSandboxRuntimeCompilePlanRequestImageKind.SNAPSHOT:
            return snapshot()
