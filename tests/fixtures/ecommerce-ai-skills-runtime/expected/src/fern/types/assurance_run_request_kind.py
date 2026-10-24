

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AssuranceRunRequestKind(enum.StrEnum):
    EVAL = "eval"
    SECURITY = "security"

    def visit(self, eval: typing.Callable[[], T_Result], security: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssuranceRunRequestKind.EVAL:
            return eval()
        if self is AssuranceRunRequestKind.SECURITY:
            return security()
