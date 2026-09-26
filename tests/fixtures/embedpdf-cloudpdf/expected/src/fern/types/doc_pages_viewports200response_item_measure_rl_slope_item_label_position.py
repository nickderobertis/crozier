

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlSlopeItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesViewports200ResponseItemMeasureRlSlopeItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocPagesViewports200ResponseItemMeasureRlSlopeItemLabelPosition.PREFIX:
            return prefix()
