

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeeCompensationsItemFlsaStatus(str, enum.Enum):
    """
    The FLSA status for this compensation.
    """

    EXEMPT = "exempt"
    SALARIED_NONEXEMPT = "salaried-nonexempt"
    NONEXEMPT = "nonexempt"
    OWNER = "owner"

    def visit(
        self,
        exempt: typing.Callable[[], T_Result],
        salaried_nonexempt: typing.Callable[[], T_Result],
        nonexempt: typing.Callable[[], T_Result],
        owner: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeeCompensationsItemFlsaStatus.EXEMPT:
            return exempt()
        if self is EmployeeCompensationsItemFlsaStatus.SALARIED_NONEXEMPT:
            return salaried_nonexempt()
        if self is EmployeeCompensationsItemFlsaStatus.NONEXEMPT:
            return nonexempt()
        if self is EmployeeCompensationsItemFlsaStatus.OWNER:
            return owner()
