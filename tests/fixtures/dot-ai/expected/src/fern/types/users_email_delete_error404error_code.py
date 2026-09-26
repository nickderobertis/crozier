

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersEmailDeleteError404ErrorCode(enum.StrEnum):
    USER_NOT_FOUND = "USER_NOT_FOUND"

    def visit(self, user_not_found: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsersEmailDeleteError404ErrorCode.USER_NOT_FOUND:
            return user_not_found()
