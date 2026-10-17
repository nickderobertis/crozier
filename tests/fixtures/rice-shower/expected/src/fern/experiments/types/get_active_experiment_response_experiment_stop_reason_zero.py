

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetActiveExperimentResponseExperimentStopReasonZero(enum.StrEnum):
    MANUAL = "manual"

    def visit(self, manual: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActiveExperimentResponseExperimentStopReasonZero.MANUAL:
            return manual()
