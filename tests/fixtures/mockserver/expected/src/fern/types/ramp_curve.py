

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RampCurve(enum.StrEnum):
    """
    interpolation curve used to ramp a value across a stage: LINEAR (constant slope), QUADRATIC (ease-in), EXPONENTIAL (steeper ease-in). Only meaningful for ramp stages; ignored for holds and pauses.
    """

    LINEAR = "LINEAR"
    EXPONENTIAL = "EXPONENTIAL"
    QUADRATIC = "QUADRATIC"

    def visit(
        self,
        linear: typing.Callable[[], T_Result],
        exponential: typing.Callable[[], T_Result],
        quadratic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RampCurve.LINEAR:
            return linear()
        if self is RampCurve.EXPONENTIAL:
            return exponential()
        if self is RampCurve.QUADRATIC:
            return quadratic()
