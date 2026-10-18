

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetExperimentResponseStatus(enum.StrEnum):
    RUNNING = "running"
    COMPLETED = "completed"
    ABORTED = "aborted"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetExperimentResponseStatus.RUNNING:
            return running()
        if self is GetExperimentResponseStatus.COMPLETED:
            return completed()
        if self is GetExperimentResponseStatus.ABORTED:
            return aborted()
