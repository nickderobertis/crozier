

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowsIncludeFilterItemsRelation(enum.StrEnum):
    WORKFLOW_VERSIONS = "workflowVersions"

    def visit(self, workflow_versions: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowsIncludeFilterItemsRelation.WORKFLOW_VERSIONS:
            return workflow_versions()
