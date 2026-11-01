

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscriptionChannelType(enum.StrEnum):
    """
    Implicit Mode: Provide a channel type. Used for system-managed channels (e.g., 'rss') where the system automatically resolves or creates the channel. Mutually exclusive with 'channel_id'.
    """

    RSS = "rss"

    def visit(self, rss: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscriptionChannelType.RSS:
            return rss()
