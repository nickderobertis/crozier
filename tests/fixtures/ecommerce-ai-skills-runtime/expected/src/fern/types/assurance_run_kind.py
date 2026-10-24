

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssuranceRunKind(enum.StrEnum):
    EVAL = "eval"
    SECURITY = "security"
    RESTORE = "restore"

    def visit(
        self,
        eval: typing.Callable[[], T_Result],
        security: typing.Callable[[], T_Result],
        restore: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AssuranceRunKind.EVAL:
            return eval()
        if self is AssuranceRunKind.SECURITY:
            return security()
        if self is AssuranceRunKind.RESTORE:
            return restore()
