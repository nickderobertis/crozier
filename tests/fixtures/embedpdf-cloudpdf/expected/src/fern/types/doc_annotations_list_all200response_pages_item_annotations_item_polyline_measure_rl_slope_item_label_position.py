

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition.SUFFIX
        ):
            return suffix()
        if (
            self
            is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemPolylineMeasureRlSlopeItemLabelPosition.PREFIX
        ):
            return prefix()
