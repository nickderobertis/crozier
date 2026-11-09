

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_method import PaymentMethod
from .payment_provider_provider import PaymentProviderProvider


class PaymentProvider(UniversalBaseModel):
    provider: PaymentProviderProvider
    merchant_id: str
    supported_payment_methods: typing.List[PaymentMethod]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
