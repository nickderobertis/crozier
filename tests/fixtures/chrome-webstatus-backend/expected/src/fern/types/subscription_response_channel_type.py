

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionResponseChannelType(enum.StrEnum):
    """
    Self-describing type to allow the UI to identify the delivery mode without fetching the underlying channel.
    """

    EMAIL = "email"
    WEBHOOK = "webhook"
    RSS = "rss"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
        rss: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SubscriptionResponseChannelType.EMAIL:
            return email()
        if self is SubscriptionResponseChannelType.WEBHOOK:
            return webhook()
        if self is SubscriptionResponseChannelType.RSS:
            return rss()
