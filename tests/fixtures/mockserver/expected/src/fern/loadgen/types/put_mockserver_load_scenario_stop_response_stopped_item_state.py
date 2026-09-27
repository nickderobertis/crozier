

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioStopResponseStoppedItemState(enum.StrEnum):
    STOPPED = "STOPPED"

    def visit(self, stopped: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioStopResponseStoppedItemState.STOPPED:
            return stopped()
