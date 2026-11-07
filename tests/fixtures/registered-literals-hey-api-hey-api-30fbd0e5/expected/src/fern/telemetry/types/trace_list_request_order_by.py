

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TraceListRequestOrderBy(enum.StrEnum):
    START_TIME = "start_time"
    END_TIME = "end_time"

    def visit(self, start_time: typing.Callable[[], T_Result], end_time: typing.Callable[[], T_Result]) -> T_Result:
        if self is TraceListRequestOrderBy.START_TIME:
            return start_time()
        if self is TraceListRequestOrderBy.END_TIME:
            return end_time()
