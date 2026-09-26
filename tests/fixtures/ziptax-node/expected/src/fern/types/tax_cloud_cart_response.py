

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_address import TaxCloudAddress
from .tax_cloud_cart_item_with_tax_response import TaxCloudCartItemWithTaxResponse
from .tax_cloud_currency import TaxCloudCurrency
from .tax_cloud_exemption import TaxCloudExemption


class TaxCloudCartResponse(UniversalBaseModel):
    cart_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="cartId"),
        pydantic.Field(
            alias="cartId",
            description="Identifier of the calculated cart. Pass this to /merchant/order/create-from-cart to capture the cart as an order.",
        ),
    ]
    """
    Identifier of the calculated cart. Pass this to /merchant/order/create-from-cart to capture the cart as an order.
    """

    currency: TaxCloudCurrency = pydantic.Field()
    """
    The currency the prices and tax amounts are denominated in.
    """

    customer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Your identifier for the customer, as submitted."),
    ]
    """
    Your identifier for the customer, as submitted.
    """

    delivered_by_seller: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="deliveredBySeller"),
        pydantic.Field(
            alias="deliveredBySeller",
            description="Whether the seller delivers the order directly, as submitted (false when omitted).",
        ),
    ]
    """
    Whether the seller delivers the order directly, as submitted (false when omitted).
    """

    destination: TaxCloudAddress = pydantic.Field()
    """
    The ship-to (destination) address, as submitted.
    """

    exemption: TaxCloudExemption = pydantic.Field()
    """
    The exemption information applied to the calculation.
    """

    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[TaxCloudCartItemWithTaxResponse]],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(
            alias="lineItems", description="The submitted line items, each with its calculated tax rate and amount."
        ),
    ] = None
    """
    The submitted line items, each with its calculated tax rate and amount.
    """

    origin: TaxCloudAddress = pydantic.Field()
    """
    The ship-from (origin) address, as submitted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
