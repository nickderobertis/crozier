

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1money import V1Money


class V1Tender(UniversalBaseModel):
    """
    A tender represents a discrete monetary exchange. Square represents this
    exchange as a money object with a specific currency and amount, where the
    amount is given in the smallest denomination of the given currency.

    Square POS can accept more than one form of tender for a single payment (such
    as by splitting a bill between a credit card and a gift card). The `tender`
    field of the Payment object lists all forms of tender used for the payment.

    Split tender payments behave slightly differently from single tender payments:

    The receipt_url for a split tender corresponds only to the first tender listed
    in the tender field. To get the receipt URLs for the remaining tenders, use
    the receipt_url fields of the corresponding Tender objects.

    *A note on gift cards**: when a customer purchases a Square gift card from a
    merchant, the merchant receives the full amount of the gift card in the
    associated payment.

    When that gift card is used as a tender, the balance of the gift card is
    reduced and the merchant receives no funds. A `Tender` object with a type of
    `SQUARE_GIFT_CARD` indicates a gift card was used for some or all of the
    associated payment.
    """

    card_brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    The brand of credit card provided.
    """

    change_back_money: typing.Optional[V1Money] = None
    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee that processed the tender.
    """

    entry_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tender's unique ID.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The tender's unique ID.
    """

    is_exchange: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts needed to pay for items purchased in the exchange.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable description of the tender.
    """

    pan_suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last four digits of the provided credit card's account number.
    """

    payment_note: typing.Optional[str] = pydantic.Field(default=None)
    """
    Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender with the type: OTHER.
    """

    receipt_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the receipt for the tender.
    """

    refunded_money: typing.Optional[V1Money] = None
    settled_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the tender was settled, in ISO 8601 format.
    """

    tendered_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the tender was created, in ISO 8601 format.
    """

    tendered_money: typing.Optional[V1Money] = None
    total_money: typing.Optional[V1Money] = None
    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of tender.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
