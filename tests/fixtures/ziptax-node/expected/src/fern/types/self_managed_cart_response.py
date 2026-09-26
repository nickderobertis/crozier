

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .self_managed_cart_item_with_tax_response import SelfManagedCartItemWithTaxResponse
from .tax_cloud_address import TaxCloudAddress
from .tax_cloud_currency import TaxCloudCurrency


class SelfManagedCartResponse(UniversalBaseModel):
    cart_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="cartId"),
        pydantic.Field(
            alias="cartId",
            description="Identifier of the calculated cart: the cartId you submitted, or a generated one when you omitted it. Self-managed calculations are not persisted, so this identifier is for correlating the response with the request only and cannot be used with /merchant/order/create-from-cart.",
        ),
    ]
    """
    Identifier of the calculated cart: the cartId you submitted, or a generated one when you omitted it. Self-managed calculations are not persisted, so this identifier is for correlating the response with the request only and cannot be used with /merchant/order/create-from-cart.
    """

    currency: TaxCloudCurrency = pydantic.Field()
    """
    The currency the prices and tax amounts are denominated in. Always USD for self-managed merchants.
    """

    customer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerId"),
        pydantic.Field(alias="customerId", description="Your identifier for the customer, as submitted."),
    ]
    """
    Your identifier for the customer, as submitted.
    """

    destination: TaxCloudAddress = pydantic.Field()
    """
    The ship-to (destination) address, as submitted.
    """

    line_items: typing_extensions.Annotated[
        typing.Optional[typing.List[SelfManagedCartItemWithTaxResponse]],
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
