

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMockserverLoadScenarioResponseStatus(enum.StrEnum):
    CLEARED = "cleared"

    def visit(self, cleared: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMockserverLoadScenarioResponseStatus.CLEARED:
            return cleared()
