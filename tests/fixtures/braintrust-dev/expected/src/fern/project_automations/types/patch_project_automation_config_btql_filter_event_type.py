

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectAutomationConfigBtqlFilterEventType(enum.StrEnum):
    """
    The type of automation.
    """

    LOGS = "logs"

    def visit(self, logs: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectAutomationConfigBtqlFilterEventType.LOGS:
            return logs()
