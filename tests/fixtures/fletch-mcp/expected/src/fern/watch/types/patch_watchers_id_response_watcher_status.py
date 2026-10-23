

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchWatchersIdResponseWatcherStatus(enum.StrEnum):
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
        if self is PatchWatchersIdResponseWatcherStatus.ACTIVE:
            return active()
        if self is PatchWatchersIdResponseWatcherStatus.CATCHING_UP:
            return catching_up()
        if self is PatchWatchersIdResponseWatcherStatus.DEGRADED:
            return degraded()
        if self is PatchWatchersIdResponseWatcherStatus.PAUSED:
            return paused()
