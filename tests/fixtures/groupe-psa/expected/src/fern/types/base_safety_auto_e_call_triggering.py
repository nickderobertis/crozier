

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaseSafetyAutoECallTriggering(enum.StrEnum):
    NOT_DETECTED = "NotDetected"
    DETECTED = "Detected"
    SHOCK_DETECTION_UNABLED = "ShockDetectionUnabled"

    def visit(
        self,
        not_detected: typing.Callable[[], T_Result],
        detected: typing.Callable[[], T_Result],
        shock_detection_unabled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BaseSafetyAutoECallTriggering.NOT_DETECTED:
            return not_detected()
        if self is BaseSafetyAutoECallTriggering.DETECTED:
            return detected()
        if self is BaseSafetyAutoECallTriggering.SHOCK_DETECTION_UNABLED:
            return shock_detection_unabled()
