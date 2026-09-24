

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectBudgetType(enum.StrEnum):
    H = "H"
    M = "M"
    EMPTY = ""

    def visit(
        self, h: typing.Callable[[], T_Result], m: typing.Callable[[], T_Result], empty: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is V1ProjectBudgetType.H:
            return h()
        if self is V1ProjectBudgetType.M:
            return m()
        if self is V1ProjectBudgetType.EMPTY:
            return empty()
