

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowertrainBaseStatus(enum.StrEnum):
    """
    Status of the powertrain
    """

    NOT_RUNNING = "NotRunning"
    STARTING = "Starting"
    RUNNING = "Running"
    STOPPING = "Stopping"
    STOPPED = "Stopped"

    def visit(
        self,
        not_running: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowertrainBaseStatus.NOT_RUNNING:
            return not_running()
        if self is PowertrainBaseStatus.STARTING:
            return starting()
        if self is PowertrainBaseStatus.RUNNING:
            return running()
        if self is PowertrainBaseStatus.STOPPING:
            return stopping()
        if self is PowertrainBaseStatus.STOPPED:
            return stopped()
