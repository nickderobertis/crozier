

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetDetectStackSetDriftRequestAction(str, enum.Enum):
    DETECT_STACK_SET_DRIFT = "DetectStackSetDrift"

    def visit(self, detect_stack_set_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetDetectStackSetDriftRequestAction.DETECT_STACK_SET_DRIFT:
            return detect_stack_set_drift()
