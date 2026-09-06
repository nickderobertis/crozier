

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class RunEvalParentObjectIdObjectType(enum.StrEnum):
    PROJECT_LOGS = "project_logs"
    EXPERIMENT = "experiment"
    PLAYGROUND_LOGS = "playground_logs"

    def visit(
        self,
        project_logs: typing.Callable[[], T_Result],
        experiment: typing.Callable[[], T_Result],
        playground_logs: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunEvalParentObjectIdObjectType.PROJECT_LOGS:
            return project_logs()
        if self is RunEvalParentObjectIdObjectType.EXPERIMENT:
            return experiment()
        if self is RunEvalParentObjectIdObjectType.PLAYGROUND_LOGS:
            return playground_logs()
