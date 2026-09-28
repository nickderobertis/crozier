

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMockserverChaosExperimentResponseStatus(enum.StrEnum):
    STOPPED = "stopped"

    def visit(self, stopped: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMockserverChaosExperimentResponseStatus.STOPPED:
            return stopped()
