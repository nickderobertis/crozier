

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelMembershipType(enum.StrEnum):
    """
    The type of the channel
    """

    STANDARD = "standard"
    PRIVATE = "private"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"
    SHARED = "shared"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
        shared: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelMembershipType.STANDARD:
            return standard()
        if self is ChannelMembershipType.PRIVATE:
            return private()
        if self is ChannelMembershipType.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
        if self is ChannelMembershipType.SHARED:
            return shared()
