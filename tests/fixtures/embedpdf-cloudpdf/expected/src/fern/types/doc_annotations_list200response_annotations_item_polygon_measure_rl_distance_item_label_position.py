

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlDistanceItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlDistanceItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocAnnotationsList200ResponseAnnotationsItemPolygonMeasureRlDistanceItemLabelPosition.PREFIX:
            return prefix()
