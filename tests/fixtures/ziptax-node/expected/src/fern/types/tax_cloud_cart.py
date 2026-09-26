

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_address import TaxCloudAddress
from .tax_cloud_cart_item import TaxCloudCartItem
from .tax_cloud_currency import TaxCloudCurrency
from .tax_cloud_discounts import TaxCloudDiscounts
from .tax_cloud_exemption import TaxCloudExemption


class TaxCloudCart(UniversalBaseModel):
    cart_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cartId"),
        pydantic.Field(
            alias="cartId",
            description="Your identifier for this cart. If omitted, TaxCloud generates one and returns it in the response; either way, pass it to /merchant/order/create-from-cart to capture the cart as an order.",
        ),
    ] = None
    """
    Your identifier for this cart. If omitted, TaxCloud generates one and returns it in the response; either way, pass it to /merchant/order/create-from-cart to capture the cart as an order.
    """

    currency: TaxCloudCurrency = pydantic.Field()
    """
    The currency the line-item prices are denominated in.
    """

    customer_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="customerId"),
        pydantic.Field(
            alias="customerId",
            description="Your identifier for the customer in your own system. Used to match exemption certificates and order history.",
        ),
    ]
    """
    Your identifier for the customer in your own system. Used to match exemption certificates and order history.
    """

    delivered_by_seller: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="deliveredBySeller"),
        pydantic.Field(
            alias="deliveredBySeller",
            description="Whether the seller delivers the order directly (own vehicles) rather than via common carrier. Affects taxability of delivery charges in some states.",
        ),
    ] = None
    """
    Whether the seller delivers the order directly (own vehicles) rather than via common carrier. Affects taxability of delivery charges in some states.
    """

    destination: TaxCloudAddress = pydantic.Field()
    """
    The ship-to (destination) address of the sale. Tax is generally calculated for this address in destination-sourced states.
    """

    discounts: typing.Optional[TaxCloudDiscounts] = pydantic.Field(default=None)
    """
    Optional line-item and order-level discounts to apply. If omitted, prices are used as is.
    """

    exemption: typing.Optional[TaxCloudExemption] = pydantic.Field(default=None)
    """
    Optional exemption information for the customer. When the customer is exempt, calculated tax is zero for exempt jurisdictions.
    """

    line_items: typing_extensions.Annotated[
        typing.List[TaxCloudCartItem],
        FieldMetadata(alias="lineItems"),
        pydantic.Field(
            alias="lineItems",
            description="The line items in the cart. Tax is calculated per item and returned per item in the response.",
        ),
    ]
    """
    The line items in the cart. Tax is calculated per item and returned per item in the response.
    """

    origin: TaxCloudAddress = pydantic.Field()
    """
    The ship-from (origin) address of the sale. Used together with destination to determine sourcing and the applicable jurisdictions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
