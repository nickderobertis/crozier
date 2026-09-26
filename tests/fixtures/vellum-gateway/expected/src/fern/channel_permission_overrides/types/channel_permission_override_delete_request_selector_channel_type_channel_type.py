

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType(enum.StrEnum):
    DM = "dm"
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(
        self,
        dm: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType.DM:
            return dm()
        if self is ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType.PRIVATE:
            return private()
        if self is ChannelPermissionOverrideDeleteRequestSelectorChannelTypeChannelType.PUBLIC:
            return public()
