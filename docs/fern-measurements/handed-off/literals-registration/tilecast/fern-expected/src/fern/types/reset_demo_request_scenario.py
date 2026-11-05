

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResetDemoRequestScenario(enum.StrEnum):
    BASIC = "basic"
    KITCHEN_SINK = "kitchen-sink"

    def visit(self, basic: typing.Callable[[], T_Result], kitchen_sink: typing.Callable[[], T_Result]) -> T_Result:
        if self is ResetDemoRequestScenario.BASIC:
            return basic()
        if self is ResetDemoRequestScenario.KITCHEN_SINK:
            return kitchen_sink()
