

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadShapeMetric(enum.StrEnum):
    """
    what the shape drives: VU = concurrent virtual users (closed model); RATE = arrival rate in iterations/second (open model). A shape expands into ordinary LoadStage stages of this type.
    """

    VU = "VU"
    RATE = "RATE"

    def visit(self, vu: typing.Callable[[], T_Result], rate: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadShapeMetric.VU:
            return vu()
        if self is LoadShapeMetric.RATE:
            return rate()
