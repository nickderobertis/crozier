

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PermissionsThresholdsGetResponseAutonomous(enum.StrEnum):
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
        if self is PermissionsThresholdsGetResponseAutonomous.NONE:
            return none()
        if self is PermissionsThresholdsGetResponseAutonomous.LOW:
            return low()
        if self is PermissionsThresholdsGetResponseAutonomous.MEDIUM:
            return medium()
        if self is PermissionsThresholdsGetResponseAutonomous.HIGH:
            return high()
