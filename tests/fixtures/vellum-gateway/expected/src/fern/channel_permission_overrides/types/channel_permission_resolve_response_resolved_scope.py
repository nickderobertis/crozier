

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionResolveResponseResolvedScope(enum.StrEnum):
    WORKSPACE = "workspace"
    ADAPTER = "adapter"
    CHANNEL_TYPE = "channel_type"
    CHANNEL = "channel"

    def visit(
        self,
        workspace: typing.Callable[[], T_Result],
        adapter: typing.Callable[[], T_Result],
        channel_type: typing.Callable[[], T_Result],
        channel: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelPermissionResolveResponseResolvedScope.WORKSPACE:
            return workspace()
        if self is ChannelPermissionResolveResponseResolvedScope.ADAPTER:
            return adapter()
        if self is ChannelPermissionResolveResponseResolvedScope.CHANNEL_TYPE:
            return channel_type()
        if self is ChannelPermissionResolveResponseResolvedScope.CHANNEL:
            return channel()
