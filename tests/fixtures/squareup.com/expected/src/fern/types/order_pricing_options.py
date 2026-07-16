

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderPricingOptions(UniversalBaseModel):
    """
    Pricing options for an order. The options affect how the order's price is calculated.
    They can be used, for example, to apply automatic price adjustments that are based on preconfigured
    [pricing rules](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogPricingRule).
    """

    auto_apply_discounts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The option to determine whether pricing rule-based
    discounts are automatically applied to an order.
    """

    auto_apply_taxes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The option to determine whether rule-based taxes are automatically
    applied to an order when the criteria of the corresponding rules are met.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
