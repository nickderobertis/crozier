

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionGroundingResultMode(enum.StrEnum):
    FIELD = "field"

    def visit(self, field: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionGroundingResultMode.FIELD:
            return field()
