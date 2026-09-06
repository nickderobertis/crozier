

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicAutomationDataScopeZeroType(enum.StrEnum):
    PROJECT_LOGS = "project_logs"

    def visit(self, project_logs: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopicAutomationDataScopeZeroType.PROJECT_LOGS:
            return project_logs()
