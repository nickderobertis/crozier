

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_tax import TaxCloudTax


class TaxCloudCartItemWithTaxResponse(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    Zero-based position of the item within the cart or order.
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
        pydantic.Field(alias="originalPrice", description="The original (pre-discount) unit price, as submitted."),
    ]
    """
    The original (pre-discount) unit price, as submitted.
    """

    price: float = pydantic.Field()
    """
    The unit price tax was calculated on. When discounts were applied, this is the discounted unit price.
    """

    quantity: float = pydantic.Field()
    """
    Quantity of the item.
    """

    tax: TaxCloudTax = pydantic.Field()
    """
    The tax rate and amount calculated for this line item.
    """

    tic: typing.Optional[int] = pydantic.Field(default=None)
    """
    Taxability Information Code (TIC) the item was calculated under. Null when no TIC applies.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
