

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .additional_recipient import AdditionalRecipient
from .money import Money
from .tender_card_details import TenderCardDetails
from .tender_cash_details import TenderCashDetails


class Tender(UniversalBaseModel):
    """
    Represents a tender (i.e., a method of payment) used in a Square transaction.
    """

    additional_recipients: typing.Optional[typing.List[AdditionalRecipient]] = pydantic.Field(default=None)
    """
    Additional recipients (other than the merchant) receiving a portion of this tender.
    For example, fees assessed on the purchase by a third party integration.
    """

    amount_money: typing.Optional[Money] = None
    card_details: typing.Optional[TenderCardDetails] = None
    cash_details: typing.Optional[TenderCashDetails] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for when the tender was created, in RFC 3339 format.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    If the tender is associated with a customer or represents a customer's card on file,
    this is the ID of the associated customer.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tender's unique ID.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the transaction's associated location.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional note associated with the tender at the time of payment.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [Payment](https://developer.squareup.com/reference/square_2021-08-18/objects/Payment) that corresponds to this tender.
    This value is only present for payments created with the v2 Payments API.
    """

    processing_fee_money: typing.Optional[Money] = None
    tip_money: typing.Optional[Money] = None
    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tender's associated transaction.
    """

    type: str = pydantic.Field()
    """
    The type of tender, such as `CARD` or `CASH`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
