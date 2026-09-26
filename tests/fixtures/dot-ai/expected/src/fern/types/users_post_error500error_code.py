

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UsersPostError500ErrorCode(enum.StrEnum):
    USER_MANAGEMENT_ERROR = "USER_MANAGEMENT_ERROR"

    def visit(self, user_management_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is UsersPostError500ErrorCode.USER_MANAGEMENT_ERROR:
            return user_management_error()
