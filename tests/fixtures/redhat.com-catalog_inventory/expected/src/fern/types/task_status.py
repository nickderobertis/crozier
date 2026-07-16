

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskStatus(enum.StrEnum):
    OK = "ok"
    WARN = "warn"
    UNCHANGED = "unchanged"
    ERROR = "error"

    def visit(
        self,
        ok: typing.Callable[[], T_Result],
        warn: typing.Callable[[], T_Result],
        unchanged: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskStatus.OK:
            return ok()
        if self is TaskStatus.WARN:
            return warn()
        if self is TaskStatus.UNCHANGED:
            return unchanged()
        if self is TaskStatus.ERROR:
            return error()
