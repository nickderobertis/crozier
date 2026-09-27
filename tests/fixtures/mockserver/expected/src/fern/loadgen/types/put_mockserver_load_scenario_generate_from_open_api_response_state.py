

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioGenerateFromOpenApiResponseState(enum.StrEnum):
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
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseState.LOADED:
            return loaded()
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseState.PENDING:
            return pending()
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseState.RUNNING:
            return running()
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseState.COMPLETED:
            return completed()
        if self is PutMockserverLoadScenarioGenerateFromOpenApiResponseState.STOPPED:
            return stopped()
