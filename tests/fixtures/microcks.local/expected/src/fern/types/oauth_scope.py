

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    ADMIN = "admin"
    """
    Administrator of the Microcks instance
    """

    MANAGER = "manager"
    """
    Services & APIs content manager
    """

    USER = "user"
    """
    Simple authenticated user
    """

    def visit(
        self,
        admin: typing.Callable[[], T_Result],
        manager: typing.Callable[[], T_Result],
        user: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OauthScope.ADMIN:
            return admin()
        if self is OauthScope.MANAGER:
            return manager()
        if self is OauthScope.USER:
            return user()
