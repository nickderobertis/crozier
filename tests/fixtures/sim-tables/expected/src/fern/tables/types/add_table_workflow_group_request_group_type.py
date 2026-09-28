

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AddTableWorkflowGroupRequestGroupType(enum.StrEnum):
    """
    Workflow-group producer type.
    """

    MANUAL = "manual"
    ENRICHMENT = "enrichment"

    def visit(self, manual: typing.Callable[[], T_Result], enrichment: typing.Callable[[], T_Result]) -> T_Result:
        if self is AddTableWorkflowGroupRequestGroupType.MANUAL:
            return manual()
        if self is AddTableWorkflowGroupRequestGroupType.ENRICHMENT:
            return enrichment()
