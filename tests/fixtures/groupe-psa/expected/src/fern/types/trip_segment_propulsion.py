

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TripSegmentPropulsion(enum.StrEnum):
    """
    Propulsion during this trip segment.
    """

    THERMAL = "Thermal"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"

    def visit(
        self,
        thermal: typing.Callable[[], T_Result],
        electric: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TripSegmentPropulsion.THERMAL:
            return thermal()
        if self is TripSegmentPropulsion.ELECTRIC:
            return electric()
        if self is TripSegmentPropulsion.HYBRID:
            return hybrid()
