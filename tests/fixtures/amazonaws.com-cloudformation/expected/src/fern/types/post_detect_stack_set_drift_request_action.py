

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDetectStackSetDriftRequestAction(enum.StrEnum):
    DETECT_STACK_SET_DRIFT = "DetectStackSetDrift"

    def visit(self, detect_stack_set_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDetectStackSetDriftRequestAction.DETECT_STACK_SET_DRIFT:
            return detect_stack_set_drift()
