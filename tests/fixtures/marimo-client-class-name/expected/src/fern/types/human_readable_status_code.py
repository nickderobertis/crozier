

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class HumanReadableStatusCode(enum.StrEnum):
    ERROR = "error"
    OK = "ok"

    def visit(self, error: typing.Callable[[], T_Result], ok: typing.Callable[[], T_Result]) -> T_Result:
        if self is HumanReadableStatusCode.ERROR:
            return error()
        if self is HumanReadableStatusCode.OK:
            return ok()
