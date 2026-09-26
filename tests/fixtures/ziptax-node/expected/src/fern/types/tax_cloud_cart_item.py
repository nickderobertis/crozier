

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TaxCloudCartItem(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the item within the cart. Each line item must have a unique index.
    """

    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(
            alias="itemId",
            description="Your unique identifier for the line item (e.g. SKU or line reference). Used to match line items in later order, refund, and discount operations.",
        ),
    ]
    """
    Your unique identifier for the line item (e.g. SKU or line reference). Used to match line items in later order, refund, and discount operations.
    """

    price: float = pydantic.Field()
    """
    Unit price of the item, in the cart's currency. When discounts are provided, this must be the pre-discount (original) price; tax is calculated on the discounted amount. Self-managed merchants only: both the unit price and the extended price (price * quantity) must be at most 1e12.
    """

    product_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="productId"),
        pydantic.Field(
            alias="productId",
            description="Unique ID of the product in the merchant's TaxCloud product catalog (e.g. SKU). Must match an existing catalog product when provided.",
        ),
    ] = None
    """
    Unique ID of the product in the merchant's TaxCloud product catalog (e.g. SKU). Must match an existing catalog product when provided.
    """

    quantity: float = pydantic.Field()
    """
    Quantity of the item. Fractional quantities are allowed. For quantities above the maximum, send a single line with quantity 1 and the extended (total) amount as the price.
    """

    tic: typing.Optional[int] = pydantic.Field(default=None)
    """
    Taxability Information Code (TIC) classifying the product for product-specific tax rules (e.g. 11010 for shipping). Defaults to 0 (general tangible goods) when omitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
