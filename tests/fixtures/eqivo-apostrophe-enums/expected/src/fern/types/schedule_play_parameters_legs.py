

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SchedulePlayParametersLegs(enum.StrEnum):
    """
    Call leg(s) for which the media will be played; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
    """

    ALEG = "aleg"
    BLEG = "bleg"
    BOTH = "both"

    def visit(
        self,
        aleg: typing.Callable[[], T_Result],
        bleg: typing.Callable[[], T_Result],
        both: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SchedulePlayParametersLegs.ALEG:
            return aleg()
        if self is SchedulePlayParametersLegs.BLEG:
            return bleg()
        if self is SchedulePlayParametersLegs.BOTH:
            return both()
