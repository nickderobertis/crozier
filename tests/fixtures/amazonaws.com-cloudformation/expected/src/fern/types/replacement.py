

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Replacement(enum.StrEnum):
    TRUE = "True"
    FALSE = "False"
    CONDITIONAL = "Conditional"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        conditional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Replacement.TRUE:
            return true()
        if self is Replacement.FALSE:
            return false()
        if self is Replacement.CONDITIONAL:
            return conditional()
