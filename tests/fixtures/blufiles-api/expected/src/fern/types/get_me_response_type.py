

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetMeResponseType(enum.StrEnum):
    USER = "user"
    ADMIN = "admin"

    def visit(self, user: typing.Callable[[], T_Result], admin: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetMeResponseType.USER:
            return user()
        if self is GetMeResponseType.ADMIN:
            return admin()
