

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .participant_declaration_change_delivery_partner_request_data_attributes import (
    ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes,
)
from .participant_declaration_change_delivery_partner_request_data_type import (
    ParticipantDeclarationChangeDeliveryPartnerRequestDataType,
)


class ParticipantDeclarationChangeDeliveryPartnerRequestData(UniversalBaseModel):
    """
    A participant declaration change delivery partner request
    """

    type: ParticipantDeclarationChangeDeliveryPartnerRequestDataType
    attributes: ParticipantDeclarationChangeDeliveryPartnerRequestDataAttributes = pydantic.Field()
    """
    An NPQ completed participant declaration
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
