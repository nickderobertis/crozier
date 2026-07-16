

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_listings_slug_request_shipping_rates_item_rate_currency import (
    PutListingsSlugRequestShippingRatesItemRateCurrency,
)


class PutListingsSlugRequestShippingRatesItemRate(UniversalBaseModel):
    amount: str = pydantic.Field()
    """
    The amount of money being expressed, as a POSIX-compliant decimal number
    """

    currency: PutListingsSlugRequestShippingRatesItemRateCurrency = pydantic.Field()
    """
    The currency the money will be expressed in
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
