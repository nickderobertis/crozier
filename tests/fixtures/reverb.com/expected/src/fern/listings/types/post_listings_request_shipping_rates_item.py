

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_listings_request_shipping_rates_item_rate import PostListingsRequestShippingRatesItemRate


class PostListingsRequestShippingRatesItem(UniversalBaseModel):
    rate: typing.Optional[PostListingsRequestShippingRatesItemRate] = None
    region_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country code or subregion/superregion code. Full list of codes at /api/shipping/regions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
