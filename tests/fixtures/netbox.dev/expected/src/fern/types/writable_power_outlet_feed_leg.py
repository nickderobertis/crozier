

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePowerOutletFeedLeg(str, enum.Enum):
    """
    Phase (for three-phase feeds)
    """

    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WritablePowerOutletFeedLeg.A:
            return a()
        if self is WritablePowerOutletFeedLeg.B:
            return b()
        if self is WritablePowerOutletFeedLeg.C:
            return c()
