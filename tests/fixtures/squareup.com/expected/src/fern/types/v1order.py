

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .error import Error
from .v1money import V1Money
from .v1order_history_entry import V1OrderHistoryEntry
from .v1tender import V1Tender


class V1Order(UniversalBaseModel):
    """
    V1Order
    """

    btc_price_satoshi: typing.Optional[float] = pydantic.Field(default=None)
    """
    For Bitcoin transactions, the price of the buyer's order in satoshi (100 million satoshi equals 1 BTC).
    """

    btc_receive_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    For Bitcoin transactions, the address that the buyer sent Bitcoin to.
    """

    buyer_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the order's buyer.
    """

    buyer_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the buyer when the order was created, if any.
    """

    canceled_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to CANCELED, if any.
    """

    completed_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to COMPLETED, if any
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order was created, in ISO 8601 format.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order expires if no action is taken, in ISO 8601 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order's unique identifier.
    """

    order_history: typing.Optional[typing.List[V1OrderHistoryEntry]] = pydantic.Field(default=None)
    """
    The history of actions associated with the order.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the payment associated with the order.
    """

    promo_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The promo code provided by the buyer, if any.
    """

    recipient_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the order's buyer.
    """

    recipient_phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number to use for the order's delivery.
    """

    refunded_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A note provided by the merchant when the order's state was set to REFUNDED, if any.
    """

    shipping_address: typing.Optional[Address] = None
    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the tax is an ADDITIVE tax or an INCLUSIVE tax.
    """

    subtotal_money: typing.Optional[V1Money] = None
    tender: typing.Optional[V1Tender] = None
    total_discount_money: typing.Optional[V1Money] = None
    total_price_money: typing.Optional[V1Money] = None
    total_shipping_money: typing.Optional[V1Money] = None
    total_tax_money: typing.Optional[V1Money] = None
    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the order was last modified, in ISO 8601 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
