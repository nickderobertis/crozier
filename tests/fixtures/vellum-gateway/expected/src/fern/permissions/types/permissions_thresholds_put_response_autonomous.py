

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionsThresholdsPutResponseAutonomous(enum.StrEnum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        medium: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PermissionsThresholdsPutResponseAutonomous.NONE:
            return none()
        if self is PermissionsThresholdsPutResponseAutonomous.LOW:
            return low()
        if self is PermissionsThresholdsPutResponseAutonomous.MEDIUM:
            return medium()
        if self is PermissionsThresholdsPutResponseAutonomous.HIGH:
            return high()
