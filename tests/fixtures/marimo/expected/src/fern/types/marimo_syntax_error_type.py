

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MarimoSyntaxErrorType(enum.StrEnum):
    SYNTAX = "syntax"

    def visit(self, syntax: typing.Callable[[], T_Result]) -> T_Result:
        if self is MarimoSyntaxErrorType.SYNTAX:
            return syntax()
