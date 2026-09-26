

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetSubscriptionsRequestIncludeSubscribers(enum.StrEnum):
    TRUE = "true"
    FALSE = "false"
    PARTIAL = "partial"

    def visit(
        self,
        true: typing.Callable[[], T_Result],
        false: typing.Callable[[], T_Result],
        partial: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetSubscriptionsRequestIncludeSubscribers.TRUE:
            return true()
        if self is GetSubscriptionsRequestIncludeSubscribers.FALSE:
            return false()
        if self is GetSubscriptionsRequestIncludeSubscribers.PARTIAL:
            return partial()
