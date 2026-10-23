

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatcherDelivery(enum.StrEnum):
    """
    Where this watcher's alerts are sent.
    """

    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def visit(self, telegram: typing.Callable[[], T_Result], webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is WatcherDelivery.TELEGRAM:
            return telegram()
        if self is WatcherDelivery.WEBHOOK:
            return webhook()
