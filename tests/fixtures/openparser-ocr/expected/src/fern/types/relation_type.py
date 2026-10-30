

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelationType(enum.StrEnum):
    CONTAINS = "contains"
    PRECEDES = "precedes"
    CONTINUATION_OF = "continuation_of"
    CAPTION_OF = "caption_of"
    FOOTNOTE_OF = "footnote_of"
    REFERS_TO = "refers_to"
    OVERLAPS = "overlaps"

    def visit(
        self,
        contains: typing.Callable[[], T_Result],
        precedes: typing.Callable[[], T_Result],
        continuation_of: typing.Callable[[], T_Result],
        caption_of: typing.Callable[[], T_Result],
        footnote_of: typing.Callable[[], T_Result],
        refers_to: typing.Callable[[], T_Result],
        overlaps: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelationType.CONTAINS:
            return contains()
        if self is RelationType.PRECEDES:
            return precedes()
        if self is RelationType.CONTINUATION_OF:
            return continuation_of()
        if self is RelationType.CAPTION_OF:
            return caption_of()
        if self is RelationType.FOOTNOTE_OF:
            return footnote_of()
        if self is RelationType.REFERS_TO:
            return refers_to()
        if self is RelationType.OVERLAPS:
            return overlaps()
