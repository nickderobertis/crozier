

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProgressEventStatus(enum.StrEnum):
    """
    running=进入该阶段；completed=该阶段产出就绪。
    """

    RUNNING = "running"
    COMPLETED = "completed"

    def visit(self, running: typing.Callable[[], T_Result], completed: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProgressEventStatus.RUNNING:
            return running()
        if self is ProgressEventStatus.COMPLETED:
            return completed()
