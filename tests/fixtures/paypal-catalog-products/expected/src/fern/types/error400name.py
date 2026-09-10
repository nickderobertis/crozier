

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Error400Name(enum.StrEnum):
    INVALID_REQUEST = "INVALID_REQUEST"

    def visit(self, invalid_request: typing.Callable[[], T_Result]) -> T_Result:
        if self is Error400Name.INVALID_REQUEST:
            return invalid_request()
