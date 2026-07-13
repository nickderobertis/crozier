

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .address import Address
from .amount import Amount
from .attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from .geolocation import Geolocation
from .label_monetary_account import LabelMonetaryAccount
from .request_inquiry_reference import RequestInquiryReference


class PaymentRead(UniversalBaseModel):
    address_billing: typing.Optional[Address] = pydantic.Field(default=None)
    """
    A billing Address provided with the Payment, currently unused.
    """

    address_shipping: typing.Optional[Address] = pydantic.Field(default=None)
    """
    A shipping Address provided with the Payment, currently unused.
    """

    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).
    """

    attachment: typing.Optional[typing.List[AttachmentMonetaryAccountPayment]] = pydantic.Field(default=None)
    """
    The Attachments attached to the Payment.
    """

    balance_after_mutation: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The new balance of the monetary account after the mutation.
    """

    batch_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the PaymentBatch if this Payment was part of one.
    """

    bunqto_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    When bunq.to payment is about to expire.
    """

    bunqto_share_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.to payment.
    """

    bunqto_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.to payment.
    """

    bunqto_sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub status of the bunq.to payment.
    """

    bunqto_time_responded: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the bunq.to payment was responded to.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the Payment was done.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.
    """

    geolocation: typing.Optional[Geolocation] = pydantic.Field(default=None)
    """
    The Geolocation where the Payment was done from.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the created Payment.
    """

    merchant_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional data included with the Payment specific to the merchant.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccount the Payment was made to or from (depending on whether this is an incoming or outgoing Payment).
    """

    payment_auto_allocate_instance: typing.Optional["PaymentAutoAllocateInstance"] = pydantic.Field(default=None)
    """
    A reference to the PaymentAutoAllocateInstance if it exists.
    """

    request_reference_split_the_bill: typing.Optional[typing.List[RequestInquiryReference]] = pydantic.Field(
        default=None
    )
    """
    The reference to the object used for split the bill. Can be RequestInquiry or RequestInquiryBatch
    """

    scheduled_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the JobScheduled if the Payment was scheduled.
    """

    sub_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-type of the Payment, can be PAYMENT, WITHDRAWAL, REVERSAL, REQUEST, BILLING, SCT, SDD or NLO.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of Payment, can be BUNQ, EBA_SCT, EBA_SDD, IDEAL, SWIFT or FIS (card).
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the Payment was last updated (will be updated when chat messages are received).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment_auto_allocate_instance import PaymentAutoAllocateInstance

update_forward_refs(PaymentRead)
