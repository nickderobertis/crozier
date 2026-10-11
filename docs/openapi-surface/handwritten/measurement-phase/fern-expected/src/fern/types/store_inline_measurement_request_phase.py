

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StoreInlineMeasurementRequestPhase(enum.StrEnum):
    """
    The phase permitted for a stored measurement.
    """

    PREPARATION = "preparation"
    RECORDING = "recording"

    def visit(self, preparation: typing.Callable[[], T_Result], recording: typing.Callable[[], T_Result]) -> T_Result:
        if self is StoreInlineMeasurementRequestPhase.PREPARATION:
            return preparation()
        if self is StoreInlineMeasurementRequestPhase.RECORDING:
            return recording()
