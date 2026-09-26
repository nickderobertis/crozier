

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class JobFinancialSummaryOneJobType(enum.StrEnum):
    CHARGE_UP = "Charge Up"

    def visit(self, charge_up: typing.Callable[[], T_Result]) -> T_Result:
        if self is JobFinancialSummaryOneJobType.CHARGE_UP:
            return charge_up()
