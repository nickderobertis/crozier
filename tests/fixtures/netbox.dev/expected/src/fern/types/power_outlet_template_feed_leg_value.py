

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerOutletTemplateFeedLegValue(enum.StrEnum):
    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerOutletTemplateFeedLegValue.A:
            return a()
        if self is PowerOutletTemplateFeedLegValue.B:
            return b()
        if self is PowerOutletTemplateFeedLegValue.C:
            return c()
