

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommandRunStatus(enum.StrEnum):
    FINISHED = "Finished"
    ERROR = "Error"
    TIME_LIMIT_EXCEEDED = "TimeLimitExceeded"

    def visit(
        self,
        finished: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
        time_limit_exceeded: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommandRunStatus.FINISHED:
            return finished()
        if self is CommandRunStatus.ERROR:
            return error()
        if self is CommandRunStatus.TIME_LIMIT_EXCEEDED:
            return time_limit_exceeded()
