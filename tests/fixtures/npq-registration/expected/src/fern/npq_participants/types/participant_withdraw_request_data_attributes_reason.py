

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantWithdrawRequestDataAttributesReason(enum.StrEnum):
    """
    The reason for the withdrawal
    """

    INSUFFICIENT_CAPACITY_TO_UNDERTAKE_PROGRAMME = "insufficient-capacity-to-undertake-programme"
    PERSONAL_REASON_HEALTH_OR_PREGNANCY_RELATED = "personal-reason-health-or-pregnancy-related"
    PERSONAL_REASON_MOVING_SCHOOL = "personal-reason-moving-school"
    PERSONAL_REASON_OTHER = "personal-reason-other"
    INSUFFICIENT_CAPACITY = "insufficient-capacity"
    CHANGE_IN_DEVELOPMENTAL_OR_PERSONAL_PRIORITIES = "change-in-developmental-or-personal-priorities"
    CHANGE_IN_SCHOOL_CIRCUMSTANCES = "change-in-school-circumstances"
    CHANGE_IN_SCHOOL_LEADERSHIP = "change-in-school-leadership"
    QUALITY_OF_PROGRAMME_STRUCTURE_NOT_SUITABLE = "quality-of-programme-structure-not-suitable."
    QUALITY_OF_PROGRAMME_CONTENT_NOT_SUITABLE = "quality-of-programme-content-not-suitable"
    QUALITY_OF_PROGRAMME_FACILITATION_NOT_EFFECTIVE = "quality-of-programme-facilitation-not-effective"
    QUALITY_OF_PROGRAMME_ACCESSIBILITY = "quality-of-programme-accessibility"
    QUALITY_OF_PROGRAMME_OTHER = "quality-of-programme-other"
    PROGRAMME_NOT_APPROPRIATE_FOR_ROLE_AND_CPD_NEEDS = "programme-not-appropriate-for-role-and-cpd-needs"
    STARTED_IN_ERROR = "started-in-error"
    EXPECTED_COMMITMENT_UNCLEAR = "expected-commitment-unclear"
    ASSESSMENT_REQUIREMENTS_NOT_MET = "assessment-requirements-not-met"
    CHANGE_IN_CAREER = "change-in-career"
    DISENGAGED_AND_UNRESPONSIVE = "disengaged-and-unresponsive"
    NON_PAYMENT_OF_INVOICE = "non-payment-of-invoice"
    OTHER = "other"

    def visit(
        self,
        insufficient_capacity_to_undertake_programme: typing.Callable[[], T_Result],
        personal_reason_health_or_pregnancy_related: typing.Callable[[], T_Result],
        personal_reason_moving_school: typing.Callable[[], T_Result],
        personal_reason_other: typing.Callable[[], T_Result],
        insufficient_capacity: typing.Callable[[], T_Result],
        change_in_developmental_or_personal_priorities: typing.Callable[[], T_Result],
        change_in_school_circumstances: typing.Callable[[], T_Result],
        change_in_school_leadership: typing.Callable[[], T_Result],
        quality_of_programme_structure_not_suitable: typing.Callable[[], T_Result],
        quality_of_programme_content_not_suitable: typing.Callable[[], T_Result],
        quality_of_programme_facilitation_not_effective: typing.Callable[[], T_Result],
        quality_of_programme_accessibility: typing.Callable[[], T_Result],
        quality_of_programme_other: typing.Callable[[], T_Result],
        programme_not_appropriate_for_role_and_cpd_needs: typing.Callable[[], T_Result],
        started_in_error: typing.Callable[[], T_Result],
        expected_commitment_unclear: typing.Callable[[], T_Result],
        assessment_requirements_not_met: typing.Callable[[], T_Result],
        change_in_career: typing.Callable[[], T_Result],
        disengaged_and_unresponsive: typing.Callable[[], T_Result],
        non_payment_of_invoice: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantWithdrawRequestDataAttributesReason.INSUFFICIENT_CAPACITY_TO_UNDERTAKE_PROGRAMME:
            return insufficient_capacity_to_undertake_programme()
        if self is ParticipantWithdrawRequestDataAttributesReason.PERSONAL_REASON_HEALTH_OR_PREGNANCY_RELATED:
            return personal_reason_health_or_pregnancy_related()
        if self is ParticipantWithdrawRequestDataAttributesReason.PERSONAL_REASON_MOVING_SCHOOL:
            return personal_reason_moving_school()
        if self is ParticipantWithdrawRequestDataAttributesReason.PERSONAL_REASON_OTHER:
            return personal_reason_other()
        if self is ParticipantWithdrawRequestDataAttributesReason.INSUFFICIENT_CAPACITY:
            return insufficient_capacity()
        if self is ParticipantWithdrawRequestDataAttributesReason.CHANGE_IN_DEVELOPMENTAL_OR_PERSONAL_PRIORITIES:
            return change_in_developmental_or_personal_priorities()
        if self is ParticipantWithdrawRequestDataAttributesReason.CHANGE_IN_SCHOOL_CIRCUMSTANCES:
            return change_in_school_circumstances()
        if self is ParticipantWithdrawRequestDataAttributesReason.CHANGE_IN_SCHOOL_LEADERSHIP:
            return change_in_school_leadership()
        if self is ParticipantWithdrawRequestDataAttributesReason.QUALITY_OF_PROGRAMME_STRUCTURE_NOT_SUITABLE:
            return quality_of_programme_structure_not_suitable()
        if self is ParticipantWithdrawRequestDataAttributesReason.QUALITY_OF_PROGRAMME_CONTENT_NOT_SUITABLE:
            return quality_of_programme_content_not_suitable()
        if self is ParticipantWithdrawRequestDataAttributesReason.QUALITY_OF_PROGRAMME_FACILITATION_NOT_EFFECTIVE:
            return quality_of_programme_facilitation_not_effective()
        if self is ParticipantWithdrawRequestDataAttributesReason.QUALITY_OF_PROGRAMME_ACCESSIBILITY:
            return quality_of_programme_accessibility()
        if self is ParticipantWithdrawRequestDataAttributesReason.QUALITY_OF_PROGRAMME_OTHER:
            return quality_of_programme_other()
        if self is ParticipantWithdrawRequestDataAttributesReason.PROGRAMME_NOT_APPROPRIATE_FOR_ROLE_AND_CPD_NEEDS:
            return programme_not_appropriate_for_role_and_cpd_needs()
        if self is ParticipantWithdrawRequestDataAttributesReason.STARTED_IN_ERROR:
            return started_in_error()
        if self is ParticipantWithdrawRequestDataAttributesReason.EXPECTED_COMMITMENT_UNCLEAR:
            return expected_commitment_unclear()
        if self is ParticipantWithdrawRequestDataAttributesReason.ASSESSMENT_REQUIREMENTS_NOT_MET:
            return assessment_requirements_not_met()
        if self is ParticipantWithdrawRequestDataAttributesReason.CHANGE_IN_CAREER:
            return change_in_career()
        if self is ParticipantWithdrawRequestDataAttributesReason.DISENGAGED_AND_UNRESPONSIVE:
            return disengaged_and_unresponsive()
        if self is ParticipantWithdrawRequestDataAttributesReason.NON_PAYMENT_OF_INVOICE:
            return non_payment_of_invoice()
        if self is ParticipantWithdrawRequestDataAttributesReason.OTHER:
            return other()
