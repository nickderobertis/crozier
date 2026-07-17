

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritablePowerOutletTemplateFeedLeg(enum.StrEnum):
    """
    Phase (for three-phase feeds)
    """

    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WritablePowerOutletTemplateFeedLeg.A:
            return a()
        if self is WritablePowerOutletTemplateFeedLeg.B:
            return b()
        if self is WritablePowerOutletTemplateFeedLeg.C:
            return c()
