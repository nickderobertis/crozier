

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SendDigitsParametersLeg(enum.StrEnum):
    """
    Call leg(s) to which DTMFs will be sent; `aleg` refers to the initial call leg, `bleg` refers to the bridged call leg, if applicable.
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
        if self is SendDigitsParametersLeg.ALEG:
            return aleg()
        if self is SendDigitsParametersLeg.BLEG:
            return bleg()
        if self is SendDigitsParametersLeg.BOTH:
            return both()
