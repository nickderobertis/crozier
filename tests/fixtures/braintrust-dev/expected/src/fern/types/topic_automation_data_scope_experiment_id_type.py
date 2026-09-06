

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TopicAutomationDataScopeExperimentIdType(enum.StrEnum):
    EXPERIMENT = "experiment"

    def visit(self, experiment: typing.Callable[[], T_Result]) -> T_Result:
        if self is TopicAutomationDataScopeExperimentIdType.EXPERIMENT:
            return experiment()
