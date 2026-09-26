

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_tax import TaxCloudTax


class SelfManagedCartItemWithTaxResponse(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the item within the cart, as submitted.
    """

    item_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="itemId"),
        pydantic.Field(alias="itemId", description="Your unique identifier for the line item, as submitted."),
    ]
    """
    Your unique identifier for the line item, as submitted.
    """

    original_price: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="originalPrice"),
        pydantic.Field(
            alias="originalPrice",
            description="The original unit price. Always equal to price, because discounts are not supported for self-managed merchants.",
        ),
    ]
    """
    The original unit price. Always equal to price, because discounts are not supported for self-managed merchants.
    """

    price: float = pydantic.Field()
    """
    The unit price tax was calculated on, as submitted. Discounts are not supported for self-managed merchants, so this is always the submitted price.
    """

    quantity: float = pydantic.Field()
    """
    Quantity of the item, as submitted.
    """

    tax: TaxCloudTax = pydantic.Field()
    """
    The tax rate and amount calculated for this line item. The amount is money and is rounded to two decimal places, the same precision a TaxCloud-managed cart returns; the rate keeps five decimal places.
    """

    tic: typing.Optional[int] = pydantic.Field(default=None)
    """
    Taxability Information Code (TIC) the item was calculated under, as submitted. Null when no TIC was supplied (general tangible goods).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
