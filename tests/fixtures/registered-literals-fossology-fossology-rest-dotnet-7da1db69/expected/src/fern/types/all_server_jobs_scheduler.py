

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AllServerJobsScheduler(enum.StrEnum):
    """
    Current scheduler status
    """

    RUNNING = "Running"
    STOPPED = "Stopped"

    def visit(self, running: typing.Callable[[], T_Result], stopped: typing.Callable[[], T_Result]) -> T_Result:
        if self is AllServerJobsScheduler.RUNNING:
            return running()
        if self is AllServerJobsScheduler.STOPPED:
            return stopped()
