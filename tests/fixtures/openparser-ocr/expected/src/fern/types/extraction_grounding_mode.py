

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractionGroundingMode(enum.StrEnum):
    """
    Extraction grounding mode. `none` preserves ordinary extraction. `field` requests
    verified per-leaf source citations (citation v1 emits element-level citations only).
    """

    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractionGroundingMode.NONE:
            return none()
        if self is ExtractionGroundingMode.FIELD:
            return field()
