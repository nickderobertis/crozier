

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_attributes_npq_enrolments_item_course_identifier import (
    ParticipantAttributesNpqEnrolmentsItemCourseIdentifier,
)
from .participant_attributes_npq_enrolments_item_deferral import ParticipantAttributesNpqEnrolmentsItemDeferral
from .participant_attributes_npq_enrolments_item_schedule_identifier import (
    ParticipantAttributesNpqEnrolmentsItemScheduleIdentifier,
)
from .participant_attributes_npq_enrolments_item_training_status import (
    ParticipantAttributesNpqEnrolmentsItemTrainingStatus,
)
from .participant_attributes_npq_enrolments_item_withdrawal import ParticipantAttributesNpqEnrolmentsItemWithdrawal


class ParticipantAttributesNpqEnrolmentsItem(UniversalBaseModel):
    """
    The details of an NPQ Participant enrolment
    """

    course_identifier: ParticipantAttributesNpqEnrolmentsItemCourseIdentifier = pydantic.Field()
    """
    The NPQ course this NPQ application relates to
    """

    schedule_identifier: typing.Optional[ParticipantAttributesNpqEnrolmentsItemScheduleIdentifier] = pydantic.Field(
        default=None
    )
    """
    The new schedule of the participant
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates which call-off contract would fund this participant's training. 2021 indicates a participant that has started, or will start, their training in the 2021/22 academic year. Once a provider accepts an application, they may change a participant's cohort up until the point of submitting a started declaration.
    """

    cohort_suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Differentiator when there are multiple call-off contracts within the same year
    """

    npq_application_id: str = pydantic.Field()
    """
    The ID of the NPQ application that was accepted to create this enrolment
    """

    eligible_for_funding: bool = pydantic.Field()
    """
    Indicates whether this NPQ participant would be eligible for funding from the DfE
    """

    training_status: ParticipantAttributesNpqEnrolmentsItemTrainingStatus = pydantic.Field()
    """
    The training status of the NPQ participant
    """

    school_urn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Unique Reference Number (URN) of the school where this NPQ participant is employed
    """

    targeted_delivery_funding_eligibility: bool = pydantic.Field()
    """
    Whether or not this application is eligible for Targeted Delivery Funding uplift
    """

    funded_place: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this participant’s training is being funded by DfE
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address registered for this NPQ participant
    """

    withdrawal: typing.Optional[ParticipantAttributesNpqEnrolmentsItemWithdrawal] = pydantic.Field(default=None)
    """
    The details of an NPQ Participant withdrawal
    """

    deferral: typing.Optional[ParticipantAttributesNpqEnrolmentsItemDeferral] = pydantic.Field(default=None)
    """
    The details of an NPQ Participant deferral
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the application was created
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
