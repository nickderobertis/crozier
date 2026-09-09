

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error500Name(enum.StrEnum):
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"

    def visit(self, internal_server_error: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error500Name.INTERNAL_SERVER_ERROR:
            return internal_server_error()
