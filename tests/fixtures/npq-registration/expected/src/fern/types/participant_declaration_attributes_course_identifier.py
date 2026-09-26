

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantDeclarationAttributesCourseIdentifier(enum.StrEnum):
    """
    The NPQ course this NPQ application relates to
    """

    NPQ_SENIOR_LEADERSHIP = "npq-senior-leadership"
    NPQ_HEADSHIP = "npq-headship"
    NPQ_EXECUTIVE_LEADERSHIP = "npq-executive-leadership"
    NPQ_EARLY_YEARS_LEADERSHIP = "npq-early-years-leadership"
    NPQ_LEADING_TEACHING = "npq-leading-teaching"
    NPQ_LEADING_BEHAVIOUR_CULTURE = "npq-leading-behaviour-culture"
    NPQ_LEADING_TEACHING_DEVELOPMENT = "npq-leading-teaching-development"
    NPQ_LEADING_LITERACY = "npq-leading-literacy"
    NPQ_LEADING_PRIMARY_MATHEMATICS = "npq-leading-primary-mathematics"
    NPQ_ADDITIONAL_SUPPORT_OFFER = "npq-additional-support-offer"
    NPQ_EARLY_HEADSHIP_COACHING_OFFER = "npq-early-headship-coaching-offer"
    NPQ_SENCO = "npq-senco"

    def visit(
        self,
        npq_senior_leadership: typing.Callable[[], T_Result],
        npq_headship: typing.Callable[[], T_Result],
        npq_executive_leadership: typing.Callable[[], T_Result],
        npq_early_years_leadership: typing.Callable[[], T_Result],
        npq_leading_teaching: typing.Callable[[], T_Result],
        npq_leading_behaviour_culture: typing.Callable[[], T_Result],
        npq_leading_teaching_development: typing.Callable[[], T_Result],
        npq_leading_literacy: typing.Callable[[], T_Result],
        npq_leading_primary_mathematics: typing.Callable[[], T_Result],
        npq_additional_support_offer: typing.Callable[[], T_Result],
        npq_early_headship_coaching_offer: typing.Callable[[], T_Result],
        npq_senco: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP:
            return npq_senior_leadership()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_HEADSHIP:
            return npq_headship()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_EXECUTIVE_LEADERSHIP:
            return npq_executive_leadership()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_EARLY_YEARS_LEADERSHIP:
            return npq_early_years_leadership()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_LEADING_TEACHING:
            return npq_leading_teaching()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_LEADING_BEHAVIOUR_CULTURE:
            return npq_leading_behaviour_culture()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_LEADING_TEACHING_DEVELOPMENT:
            return npq_leading_teaching_development()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_LEADING_LITERACY:
            return npq_leading_literacy()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_LEADING_PRIMARY_MATHEMATICS:
            return npq_leading_primary_mathematics()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_ADDITIONAL_SUPPORT_OFFER:
            return npq_additional_support_offer()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_EARLY_HEADSHIP_COACHING_OFFER:
            return npq_early_headship_coaching_offer()
        if self is ParticipantDeclarationAttributesCourseIdentifier.NPQ_SENCO:
            return npq_senco()
