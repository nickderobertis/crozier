

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserRole(enum.StrEnum):
    """
    The capabilities a user has. Roles are hierarchical: every higher role includes the rights of the lower ones, which is what {@see self::atLeast()} expresses. The backing values are the names the API has always used, so a stored row and a token claim read the same as the JSON a client receives.
    | |
    |---|
    | `Member` <br/> Can read their own organization and the people in it. |
    | `Administrator` <br/> Can invite, update and remove users within their own organization, and rename it. |
    | `PlatformAdministrator` <br/> Can manage every organization and every user in the system. |
    """

    MEMBER = "Member"
    ADMINISTRATOR = "Administrator"
    PLATFORM_ADMINISTRATOR = "PlatformAdministrator"

    def visit(
        self,
        member: typing.Callable[[], T_Result],
        administrator: typing.Callable[[], T_Result],
        platform_administrator: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserRole.MEMBER:
            return member()
        if self is UserRole.ADMINISTRATOR:
            return administrator()
        if self is UserRole.PLATFORM_ADMINISTRATOR:
            return platform_administrator()
