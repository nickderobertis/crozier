

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FleetUiMessageChunkDataChildProgressDataState(enum.StrEnum):
    NOT_STARTED = "not_started"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"
    TIMED_OUT = "timed_out"

    def visit(
        self,
        not_started: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        cancelled: typing.Callable[[], T_Result],
        timed_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FleetUiMessageChunkDataChildProgressDataState.NOT_STARTED:
            return not_started()
        if self is FleetUiMessageChunkDataChildProgressDataState.RUNNING:
            return running()
        if self is FleetUiMessageChunkDataChildProgressDataState.COMPLETED:
            return completed()
        if self is FleetUiMessageChunkDataChildProgressDataState.FAILED:
            return failed()
        if self is FleetUiMessageChunkDataChildProgressDataState.CANCELLED:
            return cancelled()
        if self is FleetUiMessageChunkDataChildProgressDataState.TIMED_OUT:
            return timed_out()
