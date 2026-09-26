

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersPostError409ErrorCode(enum.StrEnum):
    USER_CONFLICT = "USER_CONFLICT"

    def visit(self, user_conflict: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsersPostError409ErrorCode.USER_CONFLICT:
            return user_conflict()
