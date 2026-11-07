

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    USER = "user"
    """
    Dataportal user role
    """

    ADMIN = "admin"
    """
    Dataportal admin role
    """

    def visit(self, user: typing.Callable[[], T_Result], admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.USER:
            return user()
        if self is OauthScope.ADMIN:
            return admin()
