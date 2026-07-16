

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostDetectStackDriftRequestAction(enum.StrEnum):
    DETECT_STACK_DRIFT = "DetectStackDrift"

    def visit(self, detect_stack_drift: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostDetectStackDriftRequestAction.DETECT_STACK_DRIFT:
            return detect_stack_drift()
