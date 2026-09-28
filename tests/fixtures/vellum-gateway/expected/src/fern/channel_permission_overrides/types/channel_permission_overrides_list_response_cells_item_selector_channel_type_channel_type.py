

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType(enum.StrEnum):
    DM = "dm"
    PRIVATE = "private"
    PUBLIC = "public"

    def visit(
        self,
        dm: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType.DM:
            return dm()
        if self is ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType.PRIVATE:
            return private()
        if self is ChannelPermissionOverridesListResponseCellsItemSelectorChannelTypeChannelType.PUBLIC:
            return public()
