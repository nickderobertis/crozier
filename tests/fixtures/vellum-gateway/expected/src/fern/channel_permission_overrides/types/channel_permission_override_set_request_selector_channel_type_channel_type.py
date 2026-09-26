

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType(enum.StrEnum):
    DM = "dm"
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(
        self,
        dm: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType.DM:
            return dm()
        if self is ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType.PRIVATE:
            return private()
        if self is ChannelPermissionOverrideSetRequestSelectorChannelTypeChannelType.PUBLIC:
            return public()
