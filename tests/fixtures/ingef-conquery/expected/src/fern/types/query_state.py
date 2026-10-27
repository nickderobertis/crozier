

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueryState(enum.StrEnum):
    """
    Potential states of a query.
    """

    NEW = "NEW"
    RUNNING = "RUNNING"
    FAILED = "FAILED"
    DONE = "DONE"

    def visit(
        self,
        new: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        done: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueryState.NEW:
            return new()
        if self is QueryState.RUNNING:
            return running()
        if self is QueryState.FAILED:
            return failed()
        if self is QueryState.DONE:
            return done()
