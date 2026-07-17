

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDetectStackResourceDriftRequestAction(enum.StrEnum):
    DETECT_STACK_RESOURCE_DRIFT = "DetectStackResourceDrift"

    def visit(self, detect_stack_resource_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDetectStackResourceDriftRequestAction.DETECT_STACK_RESOURCE_DRIFT:
            return detect_stack_resource_drift()
