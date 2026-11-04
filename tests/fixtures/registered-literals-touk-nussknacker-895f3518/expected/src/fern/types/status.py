

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Status(enum.StrEnum):
    OK = "OK"

    def visit(self, ok: typing.Callable[[], T_Result]) -> T_Result:
        if self is Status.OK:
            return ok()
