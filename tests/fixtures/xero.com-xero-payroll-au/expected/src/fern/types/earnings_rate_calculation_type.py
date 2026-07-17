

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EarningsRateCalculationType(enum.StrEnum):
    USEEARNINGSRATE = "USEEARNINGSRATE"
    ENTEREARNINGSRATE = "ENTEREARNINGSRATE"
    ANNUALSALARY = "ANNUALSALARY"

    def visit(
        self,
        useearningsrate: typing.Callable[[], T_Result],
        enterearningsrate: typing.Callable[[], T_Result],
        annualsalary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EarningsRateCalculationType.USEEARNINGSRATE:
            return useearningsrate()
        if self is EarningsRateCalculationType.ENTEREARNINGSRATE:
            return enterearningsrate()
        if self is EarningsRateCalculationType.ANNUALSALARY:
            return annualsalary()
