

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionOverrideSetResponseCellThreshold(enum.StrEnum):
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
        if self is ChannelPermissionOverrideSetResponseCellThreshold.NONE:
            return none()
        if self is ChannelPermissionOverrideSetResponseCellThreshold.LOW:
            return low()
        if self is ChannelPermissionOverrideSetResponseCellThreshold.MEDIUM:
            return medium()
        if self is ChannelPermissionOverrideSetResponseCellThreshold.HIGH:
            return high()
