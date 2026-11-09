

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditPayStubPayBasisType(enum.StrEnum):
    """
    The explicit pay basis on the paystub (if present).
    """

    SALARY = "SALARY"
    HOURLY = "HOURLY"
    COMMISSION = "COMMISSION"

    def visit(
        self,
        salary: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
        commission: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditPayStubPayBasisType.SALARY:
            return salary()
        if self is CreditPayStubPayBasisType.HOURLY:
            return hourly()
        if self is CreditPayStubPayBasisType.COMMISSION:
            return commission()
