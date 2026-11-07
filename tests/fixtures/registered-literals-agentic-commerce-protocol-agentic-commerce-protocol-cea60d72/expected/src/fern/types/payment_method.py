

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_method_supported_card_networks_item import PaymentMethodSupportedCardNetworksItem
from .payment_method_type import PaymentMethodType


class PaymentMethod(UniversalBaseModel):
    type: PaymentMethodType
    supported_card_networks: typing.List[PaymentMethodSupportedCardNetworksItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
