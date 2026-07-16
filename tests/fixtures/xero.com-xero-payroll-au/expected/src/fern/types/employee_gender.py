

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeeGender(str, enum.Enum):
    """
    The employee’s gender. See Employee Gender
    """

    N = "N"
    M = "M"
    F = "F"
    I = "I"

    def visit(
        self,
        n: typing.Callable[[], T_Result],
        m: typing.Callable[[], T_Result],
        f: typing.Callable[[], T_Result],
        i: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeeGender.N:
            return n()
        if self is EmployeeGender.M:
            return m()
        if self is EmployeeGender.F:
            return f()
        if self is EmployeeGender.I:
            return i()
