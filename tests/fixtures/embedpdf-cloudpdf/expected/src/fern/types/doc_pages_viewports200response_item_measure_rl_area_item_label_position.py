

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocPagesViewports200ResponseItemMeasureRlAreaItemLabelPosition(enum.StrEnum):
    SUFFIX = "suffix"
    PREFIX = "prefix"

    def visit(self, suffix: typing.Callable[[], T_Result], prefix: typing.Callable[[], T_Result]) -> T_Result:
        if self is DocPagesViewports200ResponseItemMeasureRlAreaItemLabelPosition.SUFFIX:
            return suffix()
        if self is DocPagesViewports200ResponseItemMeasureRlAreaItemLabelPosition.PREFIX:
            return prefix()
