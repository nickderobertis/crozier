

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class FilterReportsRequestBilled(enum.StrEnum):
    TRUE = "true"
    FALSE = "false"

    def visit(self, true: typing.Callable[[], T_Result], false: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilterReportsRequestBilled.TRUE:
            return true()
        if self is FilterReportsRequestBilled.FALSE:
            return false()
