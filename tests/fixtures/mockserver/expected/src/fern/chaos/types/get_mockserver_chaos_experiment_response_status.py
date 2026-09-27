

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetMockserverChaosExperimentResponseStatus(enum.StrEnum):
    RUNNING = "running"
    COMPLETED = "completed"
    HALTED_BY_AUTO_HALT = "halted_by_auto_halt"
    STOPPED = "stopped"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        halted_by_auto_halt: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetMockserverChaosExperimentResponseStatus.RUNNING:
            return running()
        if self is GetMockserverChaosExperimentResponseStatus.COMPLETED:
            return completed()
        if self is GetMockserverChaosExperimentResponseStatus.HALTED_BY_AUTO_HALT:
            return halted_by_auto_halt()
        if self is GetMockserverChaosExperimentResponseStatus.STOPPED:
            return stopped()
