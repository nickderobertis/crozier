

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeResponseRole(enum.StrEnum):
    """
    当前 token 角色。
    """

    ADMIN = "admin"
    USER = "user"

    def visit(self, admin: typing.Callable[[], T_Result], user: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeResponseRole.ADMIN:
            return admin()
        if self is MeResponseRole.USER:
            return user()
