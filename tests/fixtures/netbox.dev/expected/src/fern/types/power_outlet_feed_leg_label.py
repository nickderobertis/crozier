

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerOutletFeedLegLabel(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerOutletFeedLegLabel.A:
            return a()
        if self is PowerOutletFeedLegLabel.B:
            return b()
        if self is PowerOutletFeedLegLabel.C:
            return c()
