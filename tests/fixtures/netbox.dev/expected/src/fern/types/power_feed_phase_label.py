

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PowerFeedPhaseLabel(enum.StrEnum):
    SINGLE_PHASE = "Single phase"
    THREE_PHASE = "Three-phase"

    def visit(
        self, single_phase: typing.Callable[[], T_Result], three_phase: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerFeedPhaseLabel.SINGLE_PHASE:
            return single_phase()
        if self is PowerFeedPhaseLabel.THREE_PHASE:
            return three_phase()
