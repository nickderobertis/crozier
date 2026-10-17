

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunMultitaskStrategy(enum.StrEnum):
    """
    Strategy to handle concurrent runs on the same thread.
    """

    REJECT = "reject"
    ROLLBACK = "rollback"
    INTERRUPT = "interrupt"
    ENQUEUE = "enqueue"

    def visit(
        self,
        reject: typing.Callable[[], T_Result],
        rollback: typing.Callable[[], T_Result],
        interrupt: typing.Callable[[], T_Result],
        enqueue: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunMultitaskStrategy.REJECT:
            return reject()
        if self is RunMultitaskStrategy.ROLLBACK:
            return rollback()
        if self is RunMultitaskStrategy.INTERRUPT:
            return interrupt()
        if self is RunMultitaskStrategy.ENQUEUE:
            return enqueue()
