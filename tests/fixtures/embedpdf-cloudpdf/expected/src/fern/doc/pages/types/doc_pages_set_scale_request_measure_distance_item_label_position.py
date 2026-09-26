

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesSetScaleRequestMeasureDistanceItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesSetScaleRequestMeasureDistanceItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocPagesSetScaleRequestMeasureDistanceItemLabelPosition.PREFIX:
            return prefix()
