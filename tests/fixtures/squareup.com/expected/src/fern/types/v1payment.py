

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .device import Device
from .v1money import V1Money
from .v1payment_itemization import V1PaymentItemization
from .v1payment_surcharge import V1PaymentSurcharge
from .v1payment_tax import V1PaymentTax
from .v1refund import V1Refund
from .v1tender import V1Tender


class V1Payment(UniversalBaseModel):
    """
    A payment represents a paid transaction between a Square merchant and a
    customer. Payment details are usually available from Connect API endpoints
    within a few minutes after the transaction completes.

    Each Payment object includes several fields that end in `_money`. These fields
    describe the various amounts of money that contribute to the payment total:

    <ul>
    <li>
    Monetary values are <b>positive</b> if they represent an
    <em>increase</em> in the amount of money the merchant receives (e.g.,
    <code>tax_money</code>, <code>tip_money</code>).
    </li>
    <li>
    Monetary values are <b>negative</b> if they represent an
    <em>decrease</em> in the amount of money the merchant receives (e.g.,
    <code>discount_money</code>, <code>refunded_money</code>).
    </li>
    </ul>
    """

    additive_tax: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    All of the additive taxes associated with the payment.
    """

    additive_tax_money: typing.Optional[V1Money] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the payment was created, in ISO 8601 format. Reflects the time of the first payment if the object represents an incomplete partial payment, and the time of the last or complete payment otherwise.
    """

    creator_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the Square account that took the payment.
    """

    device: typing.Optional[Device] = None
    discount_money: typing.Optional[V1Money] = None
    gross_sales_money: typing.Optional[V1Money] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment's unique identifier.
    """

    inclusive_tax: typing.Optional[typing.List[V1PaymentTax]] = pydantic.Field(default=None)
    """
    All of the inclusive taxes associated with the payment.
    """

    inclusive_tax_money: typing.Optional[V1Money] = None
    is_partial: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether or not the payment is only partially paid for.
    If true, this payment will have the tenders collected so far, but the
    itemizations will be empty until the payment is completed.
    """

    itemizations: typing.Optional[typing.List[V1PaymentItemization]] = pydantic.Field(default=None)
    """
    The items purchased in the payment.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the merchant that took the payment.
    """

    net_sales_money: typing.Optional[V1Money] = None
    net_total_money: typing.Optional[V1Money] = None
    payment_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the payment's detail page in the merchant dashboard. The merchant must be signed in to the merchant dashboard to view this page.
    """

    processing_fee_money: typing.Optional[V1Money] = None
    receipt_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the receipt for the payment. Note that for split tender
    payments, this URL corresponds to the receipt for the first tender
    listed in the payment's tender field. Each Tender object has its own
    receipt_url field you can use to get the other receipts associated with
    a split tender payment.
    """

    refunded_money: typing.Optional[V1Money] = None
    refunds: typing.Optional[typing.List[V1Refund]] = pydantic.Field(default=None)
    """
    All of the refunds applied to the payment. Note that the value of all refunds on a payment can exceed the value of all tenders if a merchant chooses to refund money to a tender after previously accepting returned goods as part of an exchange.
    """

    surcharge_money: typing.Optional[V1Money] = None
    surcharges: typing.Optional[typing.List[V1PaymentSurcharge]] = pydantic.Field(default=None)
    """
    A list of all surcharges associated with the payment.
    """

    swedish_rounding_money: typing.Optional[V1Money] = None
    tax_money: typing.Optional[V1Money] = None
    tender: typing.Optional[typing.List[V1Tender]] = pydantic.Field(default=None)
    """
    All of the tenders associated with the payment.
    """

    tip_money: typing.Optional[V1Money] = None
    total_collected_money: typing.Optional[V1Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
