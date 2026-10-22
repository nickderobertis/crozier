

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddMemberRequestRole(enum.StrEnum):
    """
    Role to assign to the user
    """

    ADMINISTRATOR = "Administrator"
    DEVELOPER = "Developer"
    ANALYST = "Analyst"
    BILLING_MANAGER = "Billing Manager"

    def visit(
        self,
        administrator: typing.Callable[[], T_Result],
        developer: typing.Callable[[], T_Result],
        analyst: typing.Callable[[], T_Result],
        billing_manager: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AddMemberRequestRole.ADMINISTRATOR:
            return administrator()
        if self is AddMemberRequestRole.DEVELOPER:
            return developer()
        if self is AddMemberRequestRole.ANALYST:
            return analyst()
        if self is AddMemberRequestRole.BILLING_MANAGER:
            return billing_manager()
