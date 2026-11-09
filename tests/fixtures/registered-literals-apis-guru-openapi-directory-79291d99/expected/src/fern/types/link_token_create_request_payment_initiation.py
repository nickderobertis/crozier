

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenCreateRequestPaymentInitiation(UniversalBaseModel):
    """
    Specifies options for initializing Link for use with the Payment Initiation (Europe) product. This field is required if `payment_initiation` is included in the `products` array. Either `payment_id` or `consent_id` must be provided.
    """

    consent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `consent_id` provided by the `/payment_initiation/consent/create` endpoint.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `payment_id` provided by the `/payment_initiation/payment/create` endpoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
