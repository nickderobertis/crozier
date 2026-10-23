

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateUserResponseRole(enum.StrEnum):
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
        if self is UpdateUserResponseRole.OWNER:
            return owner()
        if self is UpdateUserResponseRole.MANAGER:
            return manager()
        if self is UpdateUserResponseRole.MEMBER:
            return member()
