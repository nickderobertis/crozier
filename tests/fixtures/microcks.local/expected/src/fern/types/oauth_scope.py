

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class OauthScope(str, enum.Enum):
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
