

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tax_cloud_order_level_discount_type import TaxCloudOrderLevelDiscountType


class TaxCloudOrderLevelDiscount(UniversalBaseModel):
    type: TaxCloudOrderLevelDiscountType = pydantic.Field()
    """
    The kind of discount: 'percentage' (a fraction of the order total) or 'amount' (a fixed currency amount).
    """

    value: float = pydantic.Field()
    """
    The discount value: a decimal fraction between 0 and 1 for 'percentage', or a currency amount for 'amount'. When discounts are provided, line-item prices must be pre-discount (original) prices.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
