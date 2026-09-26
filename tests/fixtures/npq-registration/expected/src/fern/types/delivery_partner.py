

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery_partner_attributes import DeliveryPartnerAttributes
from .delivery_partner_type import DeliveryPartnerType
from .id_attribute import IdAttribute


class DeliveryPartner(UniversalBaseModel):
    """
    A single delivery partner
    """

    id: IdAttribute
    type: DeliveryPartnerType = pydantic.Field()
    """
    The data type
    """

    attributes: DeliveryPartnerAttributes

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
