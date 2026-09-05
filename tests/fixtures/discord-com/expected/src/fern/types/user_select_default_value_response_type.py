

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSelectDefaultValueResponseType(enum.StrEnum):
    USER = "user"

    def visit(self, user: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserSelectDefaultValueResponseType.USER:
            return user()
