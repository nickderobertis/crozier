

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompactionTriggerType(enum.StrEnum):
    """
    Triggered because estimated context crossed the compaction threshold.
    """

    CONTEXT_THRESHOLD_EXCEEDED = "context_threshold_exceeded"

    def visit(self, context_threshold_exceeded: typing.Callable[[], T_Result]) -> T_Result:
        if self is CompactionTriggerType.CONTEXT_THRESHOLD_EXCEEDED:
            return context_threshold_exceeded()
