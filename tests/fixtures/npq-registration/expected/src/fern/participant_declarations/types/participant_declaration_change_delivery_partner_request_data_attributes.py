

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_change_delivery_partner_request_data_attributes_declaration_type import (
    ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType,
)


class ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes(UniversalBaseModel):
    """
    An NPQ completed participant declaration
    """

    participant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique id of the participant
    """

    declaration_type: typing.Optional[
        ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributesDeclarationType
    ] = pydantic.Field(default=None)
    """
    The event declaration type
    """

    delivery_partner_id: str = pydantic.Field()
    """
    The delivery partner ID
    """

    secondary_delivery_partner_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The secondary delivery partner ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
