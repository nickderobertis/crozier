

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AccountType(enum.StrEnum):
    """
    The user type (admin vs user). If not specified in a POST request, 'user' is default
    """

    USER = "user"
    ADMIN = "admin"
    SERVICE = "service"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        admin: typing.Callable[[], T_Result],
        service: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountType.USER:
            return user()
        if self is AccountType.ADMIN:
            return admin()
        if self is AccountType.SERVICE:
            return service()
