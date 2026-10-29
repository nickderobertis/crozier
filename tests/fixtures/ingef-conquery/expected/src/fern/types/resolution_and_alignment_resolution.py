

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ResolutionAndAlignmentResolution(enum.StrEnum):
    """
    Determines the unit to sub-divide by, starting at the start of the input date range. - COMPLETE is identity, - YEARS creates subdivisions for all covered years, - QUARTERS creates subdivisions for all covered quarters, - DAYS creates subdivisions per covered day.
    """

    COMPLETE = "COMPLETE"
    DAYS = "DAYS"
    QUARTERS = "QUARTERS"
    YEARS = "YEARS"

    def visit(
        self,
        complete: typing.Callable[[], T_Result],
        days: typing.Callable[[], T_Result],
        quarters: typing.Callable[[], T_Result],
        years: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ResolutionAndAlignmentResolution.COMPLETE:
            return complete()
        if self is ResolutionAndAlignmentResolution.DAYS:
            return days()
        if self is ResolutionAndAlignmentResolution.QUARTERS:
            return quarters()
        if self is ResolutionAndAlignmentResolution.YEARS:
            return years()
