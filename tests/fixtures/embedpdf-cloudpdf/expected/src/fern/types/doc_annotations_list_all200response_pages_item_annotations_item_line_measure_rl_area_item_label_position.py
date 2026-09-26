

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAreaItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAreaItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemLineMeasureRlAreaItemLabelPosition.PREFIX:
            return prefix()
