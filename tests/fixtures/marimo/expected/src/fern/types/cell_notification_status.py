

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CellNotificationStatus(enum.StrEnum):
    DISABLED_TRANSITIVELY = "disabled-transitively"
    IDLE = "idle"
    QUEUED = "queued"
    RUNNING = "running"

    def visit(
        self,
        disabled_transitively: typing.Callable[[], T_Result],
        idle: typing.Callable[[], T_Result],
        queued: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CellNotificationStatus.DISABLED_TRANSITIVELY:
            return disabled_transitively()
        if self is CellNotificationStatus.IDLE:
            return idle()
        if self is CellNotificationStatus.QUEUED:
            return queued()
        if self is CellNotificationStatus.RUNNING:
            return running()
