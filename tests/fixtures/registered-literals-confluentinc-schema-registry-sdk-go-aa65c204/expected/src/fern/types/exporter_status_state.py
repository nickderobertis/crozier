

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExporterStatusState(enum.StrEnum):
    UNASSIGNED = "UNASSIGNED"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    PAUSED = "PAUSED"

    def visit(
        self,
        unassigned: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        paused: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExporterStatusState.UNASSIGNED:
            return unassigned()
        if self is ExporterStatusState.STARTING:
            return starting()
        if self is ExporterStatusState.RUNNING:
            return running()
        if self is ExporterStatusState.PAUSED:
            return paused()
