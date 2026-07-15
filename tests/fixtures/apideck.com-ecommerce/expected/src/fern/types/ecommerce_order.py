

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .currency import Currency
from .ecommerce_address import EcommerceAddress
from .ecommerce_discount import EcommerceDiscount
from .ecommerce_order_fulfillment_status import EcommerceOrderFulfillmentStatus
from .ecommerce_order_line_item import EcommerceOrderLineItem
from .ecommerce_order_payment_status import EcommerceOrderPaymentStatus
from .ecommerce_order_status import EcommerceOrderStatus
from .id import Id
from .linked_ecommerce_customer import LinkedEcommerceCustomer
from .tracking_item import TrackingItem
from .updated_at import UpdatedAt


class EcommerceOrder(UniversalBaseModel):
    billing_address: typing.Optional[EcommerceAddress] = None
    created_at: typing.Optional[CreatedAt] = None
    currency: typing.Optional[Currency] = None
    customer: typing.Optional[LinkedEcommerceCustomer] = None
    discounts: typing.Optional[typing.List[EcommerceDiscount]] = None
    fulfillment_status: typing.Optional[EcommerceOrderFulfillmentStatus] = pydantic.Field(default=None)
    """
    Current fulfillment status of the order.
    """

    id: typing.Optional[Id] = None
    line_items: typing.Optional[typing.List[EcommerceOrderLineItem]] = None
    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Note for the order.
    """

    order_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Order number, if any.
    """

    payment_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment method used for this order.
    """

    payment_status: typing.Optional[EcommerceOrderPaymentStatus] = pydantic.Field(default=None)
    """
    Current payment status of the order.
    """

    shipping_address: typing.Optional[EcommerceAddress] = None
    shipping_cost: typing.Optional[str] = pydantic.Field(default=None)
    """
    Shipping cost, if any.
    """

    status: typing.Optional[EcommerceOrderStatus] = None
    sub_total: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sub-total amount, normally before tax.
    """

    total_amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total amount due.
    """

    total_discount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total discount, if any.
    """

    total_tax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Total tax, if any.
    """

    tracking: typing.Optional[typing.List[TrackingItem]] = None
    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
