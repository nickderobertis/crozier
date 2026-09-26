

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition.PREFIX:
            return prefix()
