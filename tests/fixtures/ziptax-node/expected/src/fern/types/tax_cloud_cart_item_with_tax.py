

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_tax import TaxCloudTax


class TaxCloudCartItemWithTax(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the item within the order. Each line item must have a unique index.
    """

    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(
            alias="itemId",
            description="Your unique identifier for the line item (e.g. SKU or line reference). Referenced by refunds and discounts.",
        ),
    ]
    """
    Your unique identifier for the line item (e.g. SKU or line reference). Referenced by refunds and discounts.
    """

    price: float = pydantic.Field()
    """
    Unit price of the item that tax was calculated on, in the order's currency.
    """

    product_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productId"),
        pydantic.Field(
            alias="productId",
            description="Unique ID of the product in the merchant's TaxCloud product catalog. Must match an existing catalog product when provided.",
        ),
    ] = None
    """
    Unique ID of the product in the merchant's TaxCloud product catalog. Must match an existing catalog product when provided.
    """

    quantity: float = pydantic.Field()
    """
    Quantity of the item. Fractional quantities are allowed. For quantities above the maximum, send a single line with quantity 1 and the extended (total) amount as the price.
    """

    tax: TaxCloudTax = pydantic.Field()
    """
    The tax rate and amount collected for this line item. Required when creating an order directly (the amounts were computed by your checkout).
    """

    tic: typing.Optional[int] = pydantic.Field(default=None)
    """
    Taxability Information Code (TIC) classifying the product for product-specific tax rules. Defaults to 0 (general tangible goods) when omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
