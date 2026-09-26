

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .delivery_partner import DeliveryPartner


class DeliveryPartnersResponse(UniversalBaseModel):
    """
    A list of delivery partners
    """

    data: typing.List[DeliveryPartner]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
