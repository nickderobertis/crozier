

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlYItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesViewports200ResponseItemMeasureRlYItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocPagesViewports200ResponseItemMeasureRlYItemLabelPosition.PREFIX:
            return prefix()
