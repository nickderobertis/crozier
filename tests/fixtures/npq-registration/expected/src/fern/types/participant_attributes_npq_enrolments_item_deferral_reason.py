

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantAttributesNpqEnrolmentsItemDeferralReason(enum.StrEnum):
    """
    The reason a participant was deferred
    """

    BEREAVEMENT = "bereavement"
    LONG_TERM_SICKNESS = "long-term-sickness"
    PARENTAL_LEAVE = "parental-leave"
    CAREER_BREAK = "career-break"
    OTHER = "other"

    def visit(
        self,
        bereavement: typing.Callable[[], T_Result],
        long_term_sickness: typing.Callable[[], T_Result],
        parental_leave: typing.Callable[[], T_Result],
        career_break: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantAttributesNpqEnrolmentsItemDeferralReason.BEREAVEMENT:
            return bereavement()
        if self is ParticipantAttributesNpqEnrolmentsItemDeferralReason.LONG_TERM_SICKNESS:
            return long_term_sickness()
        if self is ParticipantAttributesNpqEnrolmentsItemDeferralReason.PARENTAL_LEAVE:
            return parental_leave()
        if self is ParticipantAttributesNpqEnrolmentsItemDeferralReason.CAREER_BREAK:
            return career_break()
        if self is ParticipantAttributesNpqEnrolmentsItemDeferralReason.OTHER:
            return other()
