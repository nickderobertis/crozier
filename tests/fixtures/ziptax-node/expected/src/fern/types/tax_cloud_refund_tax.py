

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaxCloudRefundTax(UniversalBaseModel):
    amount: float = pydantic.Field()
    """
    The tax amount refunded for the item, calculated proportionally from the order's tax. When the order had discounts, this reflects tax on the discounted price.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
