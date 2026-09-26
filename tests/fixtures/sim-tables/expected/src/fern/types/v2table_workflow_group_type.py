

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2TableWorkflowGroupType(enum.StrEnum):
    """
    Producer type.
    """

    MANUAL = "manual"
    ENRICHMENT = "enrichment"

    def visit(self, manual: typing.Callable[[], T_Result], enrichment: typing.Callable[[], T_Result]) -> T_Result:
        if self is V2TableWorkflowGroupType.MANUAL:
            return manual()
        if self is V2TableWorkflowGroupType.ENRICHMENT:
            return enrichment()
