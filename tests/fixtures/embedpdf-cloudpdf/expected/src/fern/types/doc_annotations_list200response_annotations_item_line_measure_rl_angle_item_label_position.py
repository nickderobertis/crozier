

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocAnnotationsList200ResponseAnnotationsItemLineMeasureRlAngleItemLabelPosition.PREFIX:
            return prefix()
