

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero(enum.StrEnum):
    AUTO = "auto"

    def visit(self, auto: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateExtractionPipelineRequestLlmOptionsReasoningEffortZero.AUTO:
            return auto()
