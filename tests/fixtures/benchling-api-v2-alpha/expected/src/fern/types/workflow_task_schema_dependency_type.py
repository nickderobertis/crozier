

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowTaskSchemaDependencyType(enum.StrEnum):
    WORKFLOW_TASK_SCHEMA = "workflow_task_schema"

    def visit(self, workflow_task_schema: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowTaskSchemaDependencyType.WORKFLOW_TASK_SCHEMA:
            return workflow_task_schema()
