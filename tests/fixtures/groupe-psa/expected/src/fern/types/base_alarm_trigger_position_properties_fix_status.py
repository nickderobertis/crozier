

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaseAlarmTriggerPositionPropertiesFixStatus(enum.StrEnum):
    """
    Fix status information is only returned when position type is set to Acquire. Horizontal & altitude position can be determined in 3D fix status mode where it is only horizontal position in 2D mode.
    """

    TWO_D = "2D"
    THREE_D = "3D"

    def visit(self, two_d: typing.Callable[[], T_Result], three_d: typing.Callable[[], T_Result]) -> T_Result:
        if self is BaseAlarmTriggerPositionPropertiesFixStatus.TWO_D:
            return two_d()
        if self is BaseAlarmTriggerPositionPropertiesFixStatus.THREE_D:
            return three_d()
