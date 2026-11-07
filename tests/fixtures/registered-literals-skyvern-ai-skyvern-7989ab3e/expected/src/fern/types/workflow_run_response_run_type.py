

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRunResponseRunType(enum.StrEnum):
    """
    Type of run - always workflow_run for workflow runs
    """

    WORKFLOW_RUN = "workflow_run"

    def visit(self, workflow_run: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowRunResponseRunType.WORKFLOW_RUN:
            return workflow_run()
