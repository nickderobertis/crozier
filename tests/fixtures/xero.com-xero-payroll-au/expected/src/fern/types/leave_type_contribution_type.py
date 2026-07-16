

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class LeaveTypeContributionType(str, enum.Enum):
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
        if self is LeaveTypeContributionType.SGC:
            return sgc()
        if self is LeaveTypeContributionType.SALARYSACRIFICE:
            return salarysacrifice()
        if self is LeaveTypeContributionType.EMPLOYERADDITIONAL:
            return employeradditional()
        if self is LeaveTypeContributionType.EMPLOYEE:
            return employee()
