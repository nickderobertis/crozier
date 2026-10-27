

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChannelRequestMembershipType(enum.StrEnum):
    STANDARD = "standard"
    PRIVATE = "private"
    SHARED = "shared"

    def visit(
        self,
        standard: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
        shared: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateChannelRequestMembershipType.STANDARD:
            return standard()
        if self is CreateChannelRequestMembershipType.PRIVATE:
            return private()
        if self is CreateChannelRequestMembershipType.SHARED:
            return shared()
