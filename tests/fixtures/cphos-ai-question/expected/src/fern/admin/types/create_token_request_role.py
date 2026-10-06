

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateTokenRequestRole(enum.StrEnum):
    """
    token 角色。
    """

    ADMIN = "admin"
    USER = "user"

    def visit(self, admin: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateTokenRequestRole.ADMIN:
            return admin()
        if self is CreateTokenRequestRole.USER:
            return user()
