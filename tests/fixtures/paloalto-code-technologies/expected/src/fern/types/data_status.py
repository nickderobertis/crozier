

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DataStatus(enum.StrEnum):
    OK = "ok"
    EMPTY = "empty"

    def visit(self, ok: typing.Callable[[], T_Result], empty: typing.Callable[[], T_Result]) -> T_Result:
        if self is DataStatus.OK:
            return ok()
        if self is DataStatus.EMPTY:
            return empty()
