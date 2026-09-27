

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioListEntryState(enum.StrEnum):
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
        if self is LoadScenarioListEntryState.LOADED:
            return loaded()
        if self is LoadScenarioListEntryState.PENDING:
            return pending()
        if self is LoadScenarioListEntryState.RUNNING:
            return running()
        if self is LoadScenarioListEntryState.COMPLETED:
            return completed()
        if self is LoadScenarioListEntryState.STOPPED:
            return stopped()
