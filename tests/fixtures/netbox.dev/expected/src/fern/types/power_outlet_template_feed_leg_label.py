

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerOutletTemplateFeedLegLabel(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"

    def visit(
        self, a: typing.Callable[[], T_Result], b: typing.Callable[[], T_Result], c: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerOutletTemplateFeedLegLabel.A:
            return a()
        if self is PowerOutletTemplateFeedLegLabel.B:
            return b()
        if self is PowerOutletTemplateFeedLegLabel.C:
            return c()
