

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetActiveExperimentResponseExperimentStopReasonOne(enum.StrEnum):
    OVERHEAT = "overheat"

    def visit(self, overheat: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActiveExperimentResponseExperimentStopReasonOne.OVERHEAT:
            return overheat()
