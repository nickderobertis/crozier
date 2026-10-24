

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DailyOpsBriefStatus(enum.StrEnum):
    COMPLETED = "completed"
    EMPTY = "empty"
    BLOCKED = "blocked"

    def visit(
        self,
        completed: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DailyOpsBriefStatus.COMPLETED:
            return completed()
        if self is DailyOpsBriefStatus.EMPTY:
            return empty()
        if self is DailyOpsBriefStatus.BLOCKED:
            return blocked()
