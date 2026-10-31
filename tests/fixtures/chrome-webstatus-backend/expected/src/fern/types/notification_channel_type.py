

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NotificationChannelType(enum.StrEnum):
    EMAIL = "email"
    WEBHOOK = "webhook"
    RSS = "rss"

    def visit(
        self,
        email: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
        rss: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NotificationChannelType.EMAIL:
            return email()
        if self is NotificationChannelType.WEBHOOK:
            return webhook()
        if self is NotificationChannelType.RSS:
            return rss()
