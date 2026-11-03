

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatchRotaCadence(enum.StrEnum):
    DAILY = "daily"
    WEEKLY = "weekly"

    def visit(self, daily: typing.Callable[[], T_Result], weekly: typing.Callable[[], T_Result]) -> T_Result:
        if self is WatchRotaCadence.DAILY:
            return daily()
        if self is WatchRotaCadence.WEEKLY:
            return weekly()
