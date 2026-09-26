

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlYItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlYItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlYItemLabelPosition.PREFIX:
            return prefix()
