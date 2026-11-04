

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserDefinedErrorErrorType(enum.StrEnum):
    USER_DEFINED_ERROR = "USER_DEFINED_ERROR"

    def visit(self, user_defined_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserDefinedErrorErrorType.USER_DEFINED_ERROR:
            return user_defined_error()
