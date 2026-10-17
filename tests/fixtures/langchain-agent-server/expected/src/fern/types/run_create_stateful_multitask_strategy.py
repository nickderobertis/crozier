

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunCreateStatefulMultitaskStrategy(enum.StrEnum):
    """
    Multitask strategy to use. Must be one of 'reject', 'interrupt', 'rollback', or 'enqueue'.
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
        if self is RunCreateStatefulMultitaskStrategy.REJECT:
            return reject()
        if self is RunCreateStatefulMultitaskStrategy.ROLLBACK:
            return rollback()
        if self is RunCreateStatefulMultitaskStrategy.INTERRUPT:
            return interrupt()
        if self is RunCreateStatefulMultitaskStrategy.ENQUEUE:
            return enqueue()
