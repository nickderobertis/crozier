

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WebhookSupportVirtualWebhooksRequestRateUnit(enum.StrEnum):
    """
    The window unit for the rate.
    """

    SECOND = "second"
    MINUTE = "minute"
    HOUR = "hour"
    DAY = "day"

    def visit(
        self,
        second: typing.Callable[[], T_Result],
        minute: typing.Callable[[], T_Result],
        hour: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookSupportVirtualWebhooksRequestRateUnit.SECOND:
            return second()
        if self is WebhookSupportVirtualWebhooksRequestRateUnit.MINUTE:
            return minute()
        if self is WebhookSupportVirtualWebhooksRequestRateUnit.HOUR:
            return hour()
        if self is WebhookSupportVirtualWebhooksRequestRateUnit.DAY:
            return day()
