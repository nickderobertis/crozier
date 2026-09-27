

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverLoadScenarioStopResponseStatus(enum.StrEnum):
    STOPPED = "stopped"

    def visit(self, stopped: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverLoadScenarioStopResponseStatus.STOPPED:
            return stopped()
