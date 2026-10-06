

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskCancelAcceptedStatus(enum.StrEnum):
    """
    aborting=正在停止（运行中任务，将在阶段边界终止）；aborted=已立即终止（排队中尚未启动的任务）。
    """

    ABORTING = "aborting"
    ABORTED = "aborted"

    def visit(self, aborting: typing.Callable[[], T_Result], aborted: typing.Callable[[], T_Result]) -> T_Result:
        if self is TaskCancelAcceptedStatus.ABORTING:
            return aborting()
        if self is TaskCancelAcceptedStatus.ABORTED:
            return aborted()
