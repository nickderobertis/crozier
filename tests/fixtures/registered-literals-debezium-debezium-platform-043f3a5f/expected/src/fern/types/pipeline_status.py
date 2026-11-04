

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineStatus(enum.StrEnum):
    DEPLOYING = "DEPLOYING"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
    FAILED = "FAILED"

    def visit(
        self,
        deploying: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineStatus.DEPLOYING:
            return deploying()
        if self is PipelineStatus.RUNNING:
            return running()
        if self is PipelineStatus.STOPPED:
            return stopped()
        if self is PipelineStatus.FAILED:
            return failed()
