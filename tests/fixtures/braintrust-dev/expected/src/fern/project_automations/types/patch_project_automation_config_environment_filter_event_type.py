

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchProjectAutomationConfigEnvironmentFilterEventType(enum.StrEnum):
    """
    The type of automation.
    """

    ENVIRONMENT_UPDATE = "environment_update"

    def visit(self, environment_update: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchProjectAutomationConfigEnvironmentFilterEventType.ENVIRONMENT_UPDATE:
            return environment_update()
