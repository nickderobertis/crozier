

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier(enum.StrEnum):
    """
    The type of course the participant is enrolled in
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
        npq_senco: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_SENIOR_LEADERSHIP:
            return npq_senior_leadership()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_HEADSHIP:
            return npq_headship()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_EXECUTIVE_LEADERSHIP:
            return npq_executive_leadership()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_EARLY_YEARS_LEADERSHIP:
            return npq_early_years_leadership()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_LEADING_TEACHING:
            return npq_leading_teaching()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_LEADING_BEHAVIOUR_CULTURE:
            return npq_leading_behaviour_culture()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_LEADING_TEACHING_DEVELOPMENT:
            return npq_leading_teaching_development()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_LEADING_LITERACY:
            return npq_leading_literacy()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_LEADING_PRIMARY_MATHEMATICS:
            return npq_leading_primary_mathematics()
        if self is ParticipantOutcomeCreateRequestDataAttributesCourseIdentifier.NPQ_SENCO:
            return npq_senco()
