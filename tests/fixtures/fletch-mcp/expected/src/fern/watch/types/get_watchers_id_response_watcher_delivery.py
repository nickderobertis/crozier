

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatchersIdResponseWatcherDelivery(enum.StrEnum):
    """
    Where this watcher's alerts are sent.
    """

    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def visit(self, telegram: typing.Callable[[], T_Result], webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWatchersIdResponseWatcherDelivery.TELEGRAM:
            return telegram()
        if self is GetWatchersIdResponseWatcherDelivery.WEBHOOK:
            return webhook()
