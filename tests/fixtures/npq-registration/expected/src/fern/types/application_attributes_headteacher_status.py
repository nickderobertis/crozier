

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ApplicationAttributesHeadteacherStatus(enum.StrEnum):
    """
    Indicates whether this NPQ participant is or will be a head teacher
    """

    NO = "no"
    YES_WHEN_COURSE_STARTS = "yes_when_course_starts"
    YES_IN_FIRST_TWO_YEARS = "yes_in_first_two_years"
    YES_OVER_TWO_YEARS = "yes_over_two_years"
    YES_IN_FIRST_FIVE_YEARS = "yes_in_first_five_years"
    YES_OVER_FIVE_YEARS = "yes_over_five_years"

    def visit(
        self,
        no: typing.Callable[[], T_Result],
        yes_when_course_starts: typing.Callable[[], T_Result],
        yes_in_first_two_years: typing.Callable[[], T_Result],
        yes_over_two_years: typing.Callable[[], T_Result],
        yes_in_first_five_years: typing.Callable[[], T_Result],
        yes_over_five_years: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationAttributesHeadteacherStatus.NO:
            return no()
        if self is ApplicationAttributesHeadteacherStatus.YES_WHEN_COURSE_STARTS:
            return yes_when_course_starts()
        if self is ApplicationAttributesHeadteacherStatus.YES_IN_FIRST_TWO_YEARS:
            return yes_in_first_two_years()
        if self is ApplicationAttributesHeadteacherStatus.YES_OVER_TWO_YEARS:
            return yes_over_two_years()
        if self is ApplicationAttributesHeadteacherStatus.YES_IN_FIRST_FIVE_YEARS:
            return yes_in_first_five_years()
        if self is ApplicationAttributesHeadteacherStatus.YES_OVER_FIVE_YEARS:
            return yes_over_five_years()
