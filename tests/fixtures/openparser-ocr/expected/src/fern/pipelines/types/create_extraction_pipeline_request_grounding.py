

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateExtractionPipelineRequestGrounding(enum.StrEnum):
    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateExtractionPipelineRequestGrounding.NONE:
            return none()
        if self is CreateExtractionPipelineRequestGrounding.FIELD:
            return field()
