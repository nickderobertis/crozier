

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmployeeEmploymentRoleSubType(enum.StrEnum):
    """
    The work schedule of the employee.
    """

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    HOURLY = "hourly"

    def visit(
        self,
        full_time: typing.Callable[[], T_Result],
        part_time: typing.Callable[[], T_Result],
        hourly: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeeEmploymentRoleSubType.FULL_TIME:
            return full_time()
        if self is EmployeeEmploymentRoleSubType.PART_TIME:
            return part_time()
        if self is EmployeeEmploymentRoleSubType.HOURLY:
            return hourly()
