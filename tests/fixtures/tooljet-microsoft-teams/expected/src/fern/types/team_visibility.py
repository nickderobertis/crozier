

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TeamVisibility(enum.StrEnum):
    PRIVATE = "private"
    PUBLIC = "public"
    HIDDEN_MEMBERSHIP = "hiddenMembership"
    UNKNOWN_FUTURE_VALUE = "unknownFutureValue"

    def visit(
        self,
        private: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
        hidden_membership: typing.Callable[[], T_Result],
        unknown_future_value: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TeamVisibility.PRIVATE:
            return private()
        if self is TeamVisibility.PUBLIC:
            return public()
        if self is TeamVisibility.HIDDEN_MEMBERSHIP:
            return hidden_membership()
        if self is TeamVisibility.UNKNOWN_FUTURE_VALUE:
            return unknown_future_value()
