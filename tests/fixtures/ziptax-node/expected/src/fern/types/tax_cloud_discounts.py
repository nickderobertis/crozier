

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_line_item_discount import TaxCloudLineItemDiscount
from .tax_cloud_order_level_discount import TaxCloudOrderLevelDiscount


class TaxCloudDiscounts(UniversalBaseModel):
    line_item_discounts: typing_extensions.Annotated[
        typing.Optional[typing.List[TaxCloudLineItemDiscount]],
        FieldMetadata(alias="lineItemDiscounts"),
        pydantic.Field(
            alias="lineItemDiscounts",
            description="Discounts applied to specific line items, applied before any order-level discount. Each entry must reference a valid itemId from the lineItems array.",
        ),
    ] = None
    """
    Discounts applied to specific line items, applied before any order-level discount. Each entry must reference a valid itemId from the lineItems array.
    """

    order_discount: typing_extensions.Annotated[
        typing.Optional[TaxCloudOrderLevelDiscount],
        FieldMetadata(alias="orderDiscount"),
        pydantic.Field(
            alias="orderDiscount",
            description="A discount applied to the entire order, applied after line-item discounts. Shipping items (TICs 11010-11015) and Colorado retail delivery fees (TIC 11098) are excluded from order-level discount calculations.",
        ),
    ] = None
    """
    A discount applied to the entire order, applied after line-item discounts. Shipping items (TICs 11010-11015) and Colorado retail delivery fees (TIC 11098) are excluded from order-level discount calculations.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
