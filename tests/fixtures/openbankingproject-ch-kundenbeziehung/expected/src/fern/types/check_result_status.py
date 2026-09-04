

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckResultStatus(enum.StrEnum):
    CLEAR = "clear"
    ALERT = "alert"
    BLOCKED = "blocked"

    def visit(
        self,
        clear: typing.Callable[[], T_Result],
        alert: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CheckResultStatus.CLEAR:
            return clear()
        if self is CheckResultStatus.ALERT:
            return alert()
        if self is CheckResultStatus.BLOCKED:
            return blocked()
