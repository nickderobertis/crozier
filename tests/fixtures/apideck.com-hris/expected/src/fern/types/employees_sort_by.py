

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeesSortBy(str, enum.Enum):
    """
    The field on which to sort the Employees
    """

    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"

    def visit(
        self,
        first_name: typing.Callable[[], T_Result],
        last_name: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        updated_at: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeesSortBy.FIRST_NAME:
            return first_name()
        if self is EmployeesSortBy.LAST_NAME:
            return last_name()
        if self is EmployeesSortBy.CREATED_AT:
            return created_at()
        if self is EmployeesSortBy.UPDATED_AT:
            return updated_at()
