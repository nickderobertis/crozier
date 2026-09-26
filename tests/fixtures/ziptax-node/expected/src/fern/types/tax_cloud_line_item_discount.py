

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_line_item_discount_type import TaxCloudLineItemDiscountType


class TaxCloudLineItemDiscount(UniversalBaseModel):
    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(
            alias="itemId",
            description="The itemId of the line item this discount applies to. Must match an itemId in the lineItems array.",
        ),
    ]
    """
    The itemId of the line item this discount applies to. Must match an itemId in the lineItems array.
    """

    type: TaxCloudLineItemDiscountType = pydantic.Field()
    """
    The kind of discount: 'percentage' (a fraction of the price) or 'amount' (a fixed currency amount).
    """

    value: float = pydantic.Field()
    """
    The discount value: a decimal fraction between 0 and 1 for 'percentage' (e.g. 0.1 = 10% off), or a currency amount for 'amount'. When discounts are provided, line-item prices must be pre-discount (original) prices.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
