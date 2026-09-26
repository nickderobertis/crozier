

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier(enum.StrEnum):
    """
    The new schedule of the participant
    """

    NPQ_ASO_MARCH = "npq-aso-march"
    NPQ_ASO_JUNE = "npq-aso-june"
    NPQ_ASO_NOVEMBER = "npq-aso-november"
    NPQ_ASO_DECEMBER = "npq-aso-december"
    NPQ_EHCO_MARCH = "npq-ehco-march"
    NPQ_EHCO_JUNE = "npq-ehco-june"
    NPQ_EHCO_NOVEMBER = "npq-ehco-november"
    NPQ_EHCO_DECEMBER = "npq-ehco-december"
    NPQ_LEADERSHIP_AUTUMN = "npq-leadership-autumn"
    NPQ_LEADERSHIP_SPRING = "npq-leadership-spring"
    NPQ_SPECIALIST_AUTUMN = "npq-specialist-autumn"
    NPQ_SPECIALIST_SPRING = "npq-specialist-spring"

    def visit(
        self,
        npq_aso_march: typing.Callable[[], T_Result],
        npq_aso_june: typing.Callable[[], T_Result],
        npq_aso_november: typing.Callable[[], T_Result],
        npq_aso_december: typing.Callable[[], T_Result],
        npq_ehco_march: typing.Callable[[], T_Result],
        npq_ehco_june: typing.Callable[[], T_Result],
        npq_ehco_november: typing.Callable[[], T_Result],
        npq_ehco_december: typing.Callable[[], T_Result],
        npq_leadership_autumn: typing.Callable[[], T_Result],
        npq_leadership_spring: typing.Callable[[], T_Result],
        npq_specialist_autumn: typing.Callable[[], T_Result],
        npq_specialist_spring: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_MARCH:
            return npq_aso_march()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_JUNE:
            return npq_aso_june()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_NOVEMBER:
            return npq_aso_november()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_ASO_DECEMBER:
            return npq_aso_december()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_EHCO_MARCH:
            return npq_ehco_march()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_EHCO_JUNE:
            return npq_ehco_june()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_EHCO_NOVEMBER:
            return npq_ehco_november()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_EHCO_DECEMBER:
            return npq_ehco_december()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_LEADERSHIP_AUTUMN:
            return npq_leadership_autumn()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_LEADERSHIP_SPRING:
            return npq_leadership_spring()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_SPECIALIST_AUTUMN:
            return npq_specialist_autumn()
        if self is ParticipantChangeScheduleRequestDataAttributesScheduleIdentifier.NPQ_SPECIALIST_SPRING:
            return npq_specialist_spring()
