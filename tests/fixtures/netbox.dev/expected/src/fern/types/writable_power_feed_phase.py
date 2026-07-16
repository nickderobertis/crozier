

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WritablePowerFeedPhase(str, enum.Enum):
    SINGLE_PHASE = "single-phase"
    THREE_PHASE = "three-phase"

    def visit(
        self, single_phase: typing.Callable[[], T_Result], three_phase: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is WritablePowerFeedPhase.SINGLE_PHASE:
            return single_phase()
        if self is WritablePowerFeedPhase.THREE_PHASE:
            return three_phase()
