

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_attributes_course_identifier import ParticipantDeclarationAttributesCourseIdentifier
from .participant_declaration_attributes_declaration_type import ParticipantDeclarationAttributesDeclarationType
from .participant_declaration_attributes_ineligible_for_funding_reason import (
    ParticipantDeclarationAttributesIneligibleForFundingReason,
)
from .participant_declaration_attributes_state import ParticipantDeclarationAttributesState


class ParticipantDeclarationAttributes(UniversalBaseModel):
    participant_id: str = pydantic.Field()
    """
    The unique identifier of this participant declaration record
    """

    declaration_type: ParticipantDeclarationAttributesDeclarationType = pydantic.Field()
    """
    The event declaration type
    """

    course_identifier: ParticipantDeclarationAttributesCourseIdentifier = pydantic.Field()
    """
    The NPQ course this NPQ application relates to
    """

    declaration_date: str = pydantic.Field()
    """
    The event declaration date
    """

    state: ParticipantDeclarationAttributesState = pydantic.Field()
    """
    Indicates the state of this payment declaration
    """

    has_passed: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the participant has failed or passed
    """

    statement_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID of the statement the declaration will be paid as part of
    """

    clawback_statement_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique id of the statement to which the declaration will be clawed back on, if any
    """

    uplift_paid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If participant is eligible for uplift, whether it has been paid as part of this declaration
    """

    lead_provider_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the provider that submitted the declaration
    """

    ineligible_for_funding_reason: typing.Optional[ParticipantDeclarationAttributesIneligibleForFundingReason] = (
        pydantic.Field(default=None)
    )
    """
    If the declaration is ineligible, the reason why
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date the application was created
    """

    delivery_partner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The delivery partner ID
    """

    delivery_partner_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The delivery partner name
    """

    secondary_delivery_partner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The secondary delivery partner ID
    """

    secondary_delivery_partner_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The secondary delivery partner name
    """

    application_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the NPQ application
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The date the application was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
