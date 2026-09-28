

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionResolveResponseResolvedThreshold(enum.StrEnum):
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
        if self is ChannelPermissionResolveResponseResolvedThreshold.NONE:
            return none()
        if self is ChannelPermissionResolveResponseResolvedThreshold.LOW:
            return low()
        if self is ChannelPermissionResolveResponseResolvedThreshold.MEDIUM:
            return medium()
        if self is ChannelPermissionResolveResponseResolvedThreshold.HIGH:
            return high()
