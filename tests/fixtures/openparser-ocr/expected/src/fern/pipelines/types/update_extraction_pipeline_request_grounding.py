

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateExtractionPipelineRequestGrounding(enum.StrEnum):
    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is UpdateExtractionPipelineRequestGrounding.NONE:
            return none()
        if self is UpdateExtractionPipelineRequestGrounding.FIELD:
            return field()
