

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioReportState(enum.StrEnum):
    LOADED = "LOADED"
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    STOPPED = "STOPPED"

    def visit(
        self,
        loaded: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        completed: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoadScenarioReportState.LOADED:
            return loaded()
        if self is LoadScenarioReportState.PENDING:
            return pending()
        if self is LoadScenarioReportState.RUNNING:
            return running()
        if self is LoadScenarioReportState.COMPLETED:
            return completed()
        if self is LoadScenarioReportState.STOPPED:
            return stopped()
