

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommonResponseStatus(enum.StrEnum):
    OK = "ok"
    ERROR = "error"

    def visit(self, ok: typing.Callable[[], T_Result], error: typing.Callable[[], T_Result]) -> T_Result:
        if self is CommonResponseStatus.OK:
            return ok()
        if self is CommonResponseStatus.ERROR:
            return error()
