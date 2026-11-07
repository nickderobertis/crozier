

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocketEntryBoundary(enum.StrEnum):
    """
    Determines if it is the first docket entry or the last docket entry. This value will be set only for the first and last docket entry. For other docket entries it will be null. However, this will be set as single_docket_entry when the Case contains only one docket entry.
    """

    FIRST = "first"
    LAST = "last"
    SINGLE_DOCKET_ENTRY = "single_docket_entry"

    def visit(
        self,
        first: typing.Callable[[], T_Result],
        last: typing.Callable[[], T_Result],
        single_docket_entry: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocketEntryBoundary.FIRST:
            return first()
        if self is DocketEntryBoundary.LAST:
            return last()
        if self is DocketEntryBoundary.SINGLE_DOCKET_ENTRY:
            return single_docket_entry()
