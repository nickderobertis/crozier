

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ExtractBatchRequestItemsItemGrounding(enum.StrEnum):
    NONE = "none"
    FIELD = "field"

    def visit(self, none: typing.Callable[[], T_Result], field: typing.Callable[[], T_Result]) -> T_Result:
        if self is ExtractBatchRequestItemsItemGrounding.NONE:
            return none()
        if self is ExtractBatchRequestItemsItemGrounding.FIELD:
            return field()
