

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WorkflowRunTimelineType(enum.StrEnum):
    THOUGHT = "thought"
    BLOCK = "block"

    def visit(self, thought: typing.Callable[[], T_Result], block: typing.Callable[[], T_Result]) -> T_Result:
        if self is WorkflowRunTimelineType.THOUGHT:
            return thought()
        if self is WorkflowRunTimelineType.BLOCK:
            return block()
