

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class QueueJobStagesItem(enum.StrEnum):
    DONE = "done"
    ACTIVE = "active"
    QUEUED = "queued"

    def visit(
        self,
        done: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is QueueJobStagesItem.DONE:
            return done()
        if self is QueueJobStagesItem.ACTIVE:
            return active()
        if self is QueueJobStagesItem.QUEUED:
            return queued()
