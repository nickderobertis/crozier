

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_attributes_course_identifier import ApplicationAttributesCourseIdentifier
from .application_attributes_funding_choice import ApplicationAttributesFundingChoice
from .application_attributes_headteacher_status import ApplicationAttributesHeadteacherStatus
from .application_attributes_ineligible_for_funding_reason import ApplicationAttributesIneligibleForFundingReason
from .application_attributes_schedule_identifier import ApplicationAttributesScheduleIdentifier
from .application_attributes_status import ApplicationAttributesStatus


class ApplicationAttributes(UniversalBaseModel):
    course_identifier: typing.Optional[ApplicationAttributesCourseIdentifier] = pydantic.Field(default=None)
    """
    The NPQ course this NPQ application relates to
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address registered for this NPQ participant
    """

    email_validated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the email address has been validated
    """

    employer_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of current employer of the participant if not currently employed by school
    """

    employment_role: typing.Optional[str] = pydantic.Field(default=None)
    """
    Participant's current role in the company they are employed in if not currently employed by school
    """

    full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of this NPQ participant
    """

    funding_choice: typing.Optional[ApplicationAttributesFundingChoice] = pydantic.Field(default=None)
    """
    Indicates how this NPQ participant has said they will funded their training
    """

    headteacher_status: typing.Optional[ApplicationAttributesHeadteacherStatus] = pydantic.Field(default=None)
    """
    Indicates whether this NPQ participant is or will be a head teacher
    """

    ineligible_for_funding_reason: typing.Optional[ApplicationAttributesIneligibleForFundingReason] = pydantic.Field(
        default=None
    )
    """
    Indicates why this NPQ participant is not eligible for DfE funding
    """

    participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of this NPQ participant
    """

    private_childcare_provider_urn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Unique Reference Number (URN) of the private child care provider
    """

    teacher_reference_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Teacher Reference Number (TRN) for this NPQ participant
    """

    teacher_reference_number_validated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the Teacher Reference Number (TRN) has been validated
    """

    school_urn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Unique Reference Number (URN) of the school where this NPQ participant is employed
    """

    school_ukprn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UK Provider Reference Number (UK Provider Reference Number) of the school where this NPQ participant is employed
    """

    status: typing.Optional[ApplicationAttributesStatus] = pydantic.Field(default=None)
    """
    The current state of the NPQ application
    """

    reason_for_rejection: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason why the application was rejected by the lead provider
    """

    works_in_school: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the participant is currently employed by school
    """

    cohort: typing.Optional[str] = pydantic.Field(default=None)
    """
    Indicates which call-off contract would fund this participant's training. 2021 indicates a participant that has started, or will start, their training in the 2021/22 academic year. Once a provider accepts an application, they may change a participant's cohort up until the point of submitting a started declaration.
    """

    cohort_suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Differentiator when there are multiple call-off contracts within the same year
    """

    eligible_for_funding: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this NPQ participant would be eligible for funding from the DfE
    """

    targeted_delivery_funding_eligibility: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not this application is eligible for Targeted Delivery Funding uplift
    """

    teacher_catchment: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This field will indicate whether or not the participant is UK-based. <ul><li>If <code>true</code> then the registration relates to a participant who is UK-based.</li><li>If <code>false</code> then the registration relates to a participant who is not UK-based.</li></ul>
    """

    teacher_catchment_country: typing.Optional[str] = pydantic.Field(default=None)
    """
    This field shows the text entered by the participant during their NPQ online registration.
    """

    teacher_catchment_iso_country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    This field identifies which non-UK country the participant has registered from.
    The API uses <a href="https://www.iso.org/iso-3166-country-codes.html" class="govuk-link" rel="noreferrer noopener" target="_blank">ISO 3166 alpha-3 codes</a>, three-letter codes published by the International Organization for Standardization (ISO) to represent countries, dependent territories, and special areas of geographical interest.
    """

    itt_provider: typing.Optional[str] = pydantic.Field(default=None)
    """
    This field contains the legal name of the ITT accredited provider from the <a href="https://www.gov.uk/government/publications/accredited-initial-teacher-training-itt-providers/list-of-providers-accredited-to-deliver-itt-from-september-2024" class="govuk-link" rel="noreferrer noopener" target="_blank">list of providers</a>.
    """

    lead_mentor: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This field indicates whether the applicant is an ITT lead mentor.
    """

    funded_place: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not this participant’s training is being funded by DfE
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the application was created
    """

    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the application was last updated
    """

    schedule_identifier: typing.Optional[ApplicationAttributesScheduleIdentifier] = pydantic.Field(default=None)
    """
    The new schedule of the participant
    """

    works_as_senco: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the participant works as a SENCO (Special Educational Needs Coordinator)
    """

    senco_start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date when the participant started working as a SENCO
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
