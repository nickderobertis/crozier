

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadStageType(enum.StrEnum):
    """
    VU = closed model (hold/ramp concurrent virtual users); RATE = open model (hold/ramp an arrival rate in iterations/second); PAUSE = drive no load.
    """

    VU = "VU"
    RATE = "RATE"
    PAUSE = "PAUSE"

    def visit(
        self,
        vu: typing.Callable[[], T_Result],
        rate: typing.Callable[[], T_Result],
        pause: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadStageType.VU:
            return vu()
        if self is LoadStageType.RATE:
            return rate()
        if self is LoadStageType.PAUSE:
            return pause()
