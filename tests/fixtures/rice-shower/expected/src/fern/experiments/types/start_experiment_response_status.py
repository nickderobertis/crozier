

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StartExperimentResponseStatus(enum.StrEnum):
    RUNNING = "running"
    COMPLETED = "completed"
    ABORTED = "aborted"

    def visit(
        self,
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StartExperimentResponseStatus.RUNNING:
            return running()
        if self is StartExperimentResponseStatus.COMPLETED:
            return completed()
        if self is StartExperimentResponseStatus.ABORTED:
            return aborted()
