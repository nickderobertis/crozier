

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .put_listings_slug_request_shipping_rates_item import PutListingsSlugRequestShippingRatesItem


class PutListingsSlugRequestShipping(UniversalBaseModel):
    local: typing.Optional[bool] = pydantic.Field(default=None)
    """
    True if you offer local pickup
    """

    rates: typing.Optional[typing.List[PutListingsSlugRequestShippingRatesItem]] = pydantic.Field(default=None)
    """
    List of shipping rates. Set to null to clear rates.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
