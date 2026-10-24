

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DailyOpsBriefKind(enum.StrEnum):
    DAILY_OPS_BRIEF = "daily_ops_brief"

    def visit(self, daily_ops_brief: typing.Callable[[], T_Result]) -> T_Result:
        if self is DailyOpsBriefKind.DAILY_OPS_BRIEF:
            return daily_ops_brief()
