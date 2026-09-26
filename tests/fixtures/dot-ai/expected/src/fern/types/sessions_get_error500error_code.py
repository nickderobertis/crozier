

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SessionsGetError500ErrorCode(enum.StrEnum):
    SESSION_LIST_ERROR = "SESSION_LIST_ERROR"

    def visit(self, session_list_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is SessionsGetError500ErrorCode.SESSION_LIST_ERROR:
            return session_list_error()
