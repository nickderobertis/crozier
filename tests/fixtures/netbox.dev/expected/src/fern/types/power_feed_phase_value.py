

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerFeedPhaseValue(str, enum.Enum):
    SINGLE_PHASE = "single-phase"
    THREE_PHASE = "three-phase"

    def visit(
        self, single_phase: typing.Callable[[], T_Result], three_phase: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is PowerFeedPhaseValue.SINGLE_PHASE:
            return single_phase()
        if self is PowerFeedPhaseValue.THREE_PHASE:
            return three_phase()
