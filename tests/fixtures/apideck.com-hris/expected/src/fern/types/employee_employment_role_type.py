

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmployeeEmploymentRoleType(enum.StrEnum):
    """
    The type of employment relationship the employee has with the organization.
    """

    CONTRACTOR = "contractor"
    EMPLOYEE = "employee"
    FREELANCE = "freelance"
    TEMP = "temp"
    INTERNSHIP = "internship"
    OTHER = "other"

    def visit(
        self,
        contractor: typing.Callable[[], T_Result],
        employee: typing.Callable[[], T_Result],
        freelance: typing.Callable[[], T_Result],
        temp: typing.Callable[[], T_Result],
        internship: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeeEmploymentRoleType.CONTRACTOR:
            return contractor()
        if self is EmployeeEmploymentRoleType.EMPLOYEE:
            return employee()
        if self is EmployeeEmploymentRoleType.FREELANCE:
            return freelance()
        if self is EmployeeEmploymentRoleType.TEMP:
            return temp()
        if self is EmployeeEmploymentRoleType.INTERNSHIP:
            return internship()
        if self is EmployeeEmploymentRoleType.OTHER:
            return other()
