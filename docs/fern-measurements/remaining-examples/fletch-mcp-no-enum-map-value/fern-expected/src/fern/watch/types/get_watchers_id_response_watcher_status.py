

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetWatchersIdResponseWatcherStatus(enum.StrEnum):
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
        if self is GetWatchersIdResponseWatcherStatus.ACTIVE:
            return active()
        if self is GetWatchersIdResponseWatcherStatus.CATCHING_UP:
            return catching_up()
        if self is GetWatchersIdResponseWatcherStatus.DEGRADED:
            return degraded()
        if self is GetWatchersIdResponseWatcherStatus.PAUSED:
            return paused()
