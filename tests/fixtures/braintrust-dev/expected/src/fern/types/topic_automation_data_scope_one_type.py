

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicAutomationDataScopeOneType(enum.StrEnum):
    PROJECT_EXPERIMENTS = "project_experiments"

    def visit(self, project_experiments: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopicAutomationDataScopeOneType.PROJECT_EXPERIMENTS:
            return project_experiments()
