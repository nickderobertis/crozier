

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserType(enum.StrEnum):
    """
    Whether this is a user or an organization
    """

    USER = "user"
    ORG = "org"

    def visit(self, user: typing.Callable[[], T_Result], org: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserType.USER:
            return user()
        if self is UserType.ORG:
            return org()
