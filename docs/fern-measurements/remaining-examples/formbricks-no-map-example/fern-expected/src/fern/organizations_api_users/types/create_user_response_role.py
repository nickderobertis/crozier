

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateUserResponseRole(enum.StrEnum):
    """
    The role of the user in the organization
    """

    OWNER = "owner"
    MANAGER = "manager"
    MEMBER = "member"

    def visit(
        self,
        owner: typing.Callable[[], T_Result],
        manager: typing.Callable[[], T_Result],
        member: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateUserResponseRole.OWNER:
            return owner()
        if self is CreateUserResponseRole.MANAGER:
            return manager()
        if self is CreateUserResponseRole.MEMBER:
            return member()
