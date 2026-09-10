

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error500Message(enum.StrEnum):
    AN_INTERNAL_SERVER_ERROR_OCCURRED = "An internal server error occurred."

    def visit(self, an_internal_server_error_occurred: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error500Message.AN_INTERNAL_SERVER_ERROR_OCCURRED:
            return an_internal_server_error_occurred()
