

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MeasurementPhase(enum.StrEnum):
    """
    The phase permitted for a stored measurement.
    """

    PREPARATION = "preparation"
    RECORDING = "recording"

    def visit(self, preparation: typing.Callable[[], T_Result], recording: typing.Callable[[], T_Result]) -> T_Result:
        if self is MeasurementPhase.PREPARATION:
            return preparation()
        if self is MeasurementPhase.RECORDING:
            return recording()
