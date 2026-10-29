

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolutionAndAlignmentAlignment(enum.StrEnum):
    """
    Aligns the date-ranges that are subdivided. This helps with more uniform output formats. - NO_ALIGN will not alter the date-ranges, - DAY aligns to days, effectively the same as NO_ALIGN, - QUARTER will align to the start/end of the next quarter, - YEAR will align to the start/end of the next year
    """

    NO_ALIGN = "NO_ALIGN"
    DAY = "DAY"
    QUARTER = "QUARTER"
    YEAR = "YEAR"

    def visit(
        self,
        no_align: typing.Callable[[], T_Result],
        day: typing.Callable[[], T_Result],
        quarter: typing.Callable[[], T_Result],
        year: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResolutionAndAlignmentAlignment.NO_ALIGN:
            return no_align()
        if self is ResolutionAndAlignmentAlignment.DAY:
            return day()
        if self is ResolutionAndAlignmentAlignment.QUARTER:
            return quarter()
        if self is ResolutionAndAlignmentAlignment.YEAR:
            return year()
