

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSelectDefaultValueType(enum.StrEnum):
    USER = "user"

    def visit(self, user: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserSelectDefaultValueType.USER:
            return user()
