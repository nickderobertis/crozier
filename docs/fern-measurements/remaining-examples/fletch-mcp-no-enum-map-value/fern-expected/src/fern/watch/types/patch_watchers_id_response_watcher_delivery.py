

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchWatchersIdResponseWatcherDelivery(enum.StrEnum):
    """
    Where this watcher's alerts are sent.
    """

    TELEGRAM = "telegram"
    WEBHOOK = "webhook"

    def visit(self, telegram: typing.Callable[[], T_Result], webhook: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchWatchersIdResponseWatcherDelivery.TELEGRAM:
            return telegram()
        if self is PatchWatchersIdResponseWatcherDelivery.WEBHOOK:
            return webhook()
