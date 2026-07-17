

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuperannuationContributionType(enum.StrEnum):
    SGC = "SGC"
    SALARYSACRIFICE = "SALARYSACRIFICE"
    EMPLOYERADDITIONAL = "EMPLOYERADDITIONAL"
    EMPLOYEE = "EMPLOYEE"

    def visit(
        self,
        sgc: typing.Callable[[], T_Result],
        salarysacrifice: typing.Callable[[], T_Result],
        employeradditional: typing.Callable[[], T_Result],
        employee: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SuperannuationContributionType.SGC:
            return sgc()
        if self is SuperannuationContributionType.SALARYSACRIFICE:
            return salarysacrifice()
        if self is SuperannuationContributionType.EMPLOYERADDITIONAL:
            return employeradditional()
        if self is SuperannuationContributionType.EMPLOYEE:
            return employee()
