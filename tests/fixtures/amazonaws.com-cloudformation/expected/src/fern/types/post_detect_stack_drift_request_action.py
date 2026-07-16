

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDetectStackDriftRequestAction(str, enum.Enum):
    DETECT_STACK_DRIFT = "DetectStackDrift"

    def visit(self, detect_stack_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDetectStackDriftRequestAction.DETECT_STACK_DRIFT:
            return detect_stack_drift()
