

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUsersResponseDataItemRole(enum.StrEnum):
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
        if self is GetUsersResponseDataItemRole.OWNER:
            return owner()
        if self is GetUsersResponseDataItemRole.MANAGER:
            return manager()
        if self is GetUsersResponseDataItemRole.MEMBER:
            return member()
