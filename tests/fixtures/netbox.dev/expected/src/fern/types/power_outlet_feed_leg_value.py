

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerOutletFeedLegValue(enum.StrEnum):
    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerOutletFeedLegValue.A:
            return a()
        if self is PowerOutletFeedLegValue.B:
            return b()
        if self is PowerOutletFeedLegValue.C:
            return c()
