

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CronCreateOnRunCompleted(enum.StrEnum):
    """
    What to do with the thread after the run completes. 'delete' removes the thread after execution. 'keep' creates a new thread for each execution but does not clean them up.
    """

    DELETE = "delete"
    KEEP = "keep"

    def visit(self, delete: typing.Callable[[], T_Result], keep: typing.Callable[[], T_Result]) -> T_Result:
        if self is CronCreateOnRunCompleted.DELETE:
            return delete()
        if self is CronCreateOnRunCompleted.KEEP:
            return keep()
