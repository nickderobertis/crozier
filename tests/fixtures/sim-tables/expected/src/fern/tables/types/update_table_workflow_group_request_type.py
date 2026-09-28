

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateTableWorkflowGroupRequestType(enum.StrEnum):
    """
    Workflow-group producer type. Must match the group's stored type — a group's producer cannot be changed after creation.
    """

    MANUAL = "manual"
    ENRICHMENT = "enrichment"

    def visit(self, manual: typing.Callable[[], T_Result], enrichment: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateTableWorkflowGroupRequestType.MANUAL:
            return manual()
        if self is UpdateTableWorkflowGroupRequestType.ENRICHMENT:
            return enrichment()
