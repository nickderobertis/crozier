

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ThreadCronCreateMultitaskStrategy(enum.StrEnum):
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
        if self is ThreadCronCreateMultitaskStrategy.REJECT:
            return reject()
        if self is ThreadCronCreateMultitaskStrategy.ROLLBACK:
            return rollback()
        if self is ThreadCronCreateMultitaskStrategy.INTERRUPT:
            return interrupt()
        if self is ThreadCronCreateMultitaskStrategy.ENQUEUE:
            return enqueue()
