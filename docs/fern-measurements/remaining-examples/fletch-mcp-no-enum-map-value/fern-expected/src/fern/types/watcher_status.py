

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WatcherStatus(enum.StrEnum):
    ACTIVE = "active"
    CATCHING_UP = "catching_up"
    DEGRADED = "degraded"
    PAUSED = "paused"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        catching_up: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WatcherStatus.ACTIVE:
            return active()
        if self is WatcherStatus.CATCHING_UP:
            return catching_up()
        if self is WatcherStatus.DEGRADED:
            return degraded()
        if self is WatcherStatus.PAUSED:
            return paused()
