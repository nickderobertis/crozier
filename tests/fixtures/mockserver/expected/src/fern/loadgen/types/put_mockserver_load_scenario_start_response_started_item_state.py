

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioStartResponseStartedItemState(enum.StrEnum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"

    def visit(self, pending: typing.Callable[[], T_Result], running: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioStartResponseStartedItemState.PENDING:
            return pending()
        if self is PutMockserverLoadScenarioStartResponseStartedItemState.RUNNING:
            return running()
