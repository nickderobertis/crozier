

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ProjectBudgetCalculation(enum.StrEnum):
    PENDING = "pending"
    COMPLETED = "completed"

    def visit(self, pending: typing.Callable[[], T_Result], completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ProjectBudgetCalculation.PENDING:
            return pending()
        if self is V1ProjectBudgetCalculation.COMPLETED:
            return completed()
