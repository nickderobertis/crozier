

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineStatus(enum.StrEnum):
    """
    Workflow-controlled execution state. Updated by the Temporal workflow.
    """

    SETUP = "setup"
    BACKFILL = "backfill"
    READY = "ready"
    PAUSED = "paused"
    TEARDOWN = "teardown"
    ERROR = "error"

    def visit(
        self,
        setup: typing.Callable[[], T_Result],
        backfill: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
        teardown: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineStatus.SETUP:
            return setup()
        if self is PipelineStatus.BACKFILL:
            return backfill()
        if self is PipelineStatus.READY:
            return ready()
        if self is PipelineStatus.PAUSED:
            return paused()
        if self is PipelineStatus.TEARDOWN:
            return teardown()
        if self is PipelineStatus.ERROR:
            return error()
