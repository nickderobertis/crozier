

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostDetectStackResourceDriftRequestAction(str, enum.Enum):
    DETECT_STACK_RESOURCE_DRIFT = "DetectStackResourceDrift"

    def visit(self, detect_stack_resource_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDetectStackResourceDriftRequestAction.DETECT_STACK_RESOURCE_DRIFT:
            return detect_stack_resource_drift()
