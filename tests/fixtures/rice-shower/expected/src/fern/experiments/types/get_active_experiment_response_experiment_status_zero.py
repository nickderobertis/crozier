

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetActiveExperimentResponseExperimentStatusZero(enum.StrEnum):
    RUNNING = "running"

    def visit(self, running: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActiveExperimentResponseExperimentStatusZero.RUNNING:
            return running()
