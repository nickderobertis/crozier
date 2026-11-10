

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .external_payment_refund_details import ExternalPaymentRefundDetails
from .external_payment_schedule_get import ExternalPaymentScheduleGet
from .payment_amount import PaymentAmount
from .payment_amount_refunded import PaymentAmountRefunded
from .payment_initiation_payment_status import PaymentInitiationPaymentStatus
from .payment_scheme import PaymentScheme
from .sender_bacs_nullable import SenderBacsNullable


class PaymentInitiationPayment(UniversalBaseModel):
    """
    PaymentInitiationPayment defines a payment initiation payment
    """

    adjusted_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the reference sent to the bank after adjustment to pass bank validation rules.
    """

    adjusted_scheme: typing.Optional[PaymentScheme] = None
    amount: PaymentAmount
    amount_refunded: typing.Optional[PaymentAmountRefunded] = None
    bacs: typing.Optional[SenderBacsNullable] = None
    consent_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent.
    """

    iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The International Bank Account Number (IBAN) for the sender, if specified in the `/payment_initiation/payment/create` call.
    """

    last_status_update: dt.datetime = pydantic.Field()
    """
    The date and time of the last time the `status` was updated, in IS0 8601 format
    """

    payment_id: str = pydantic.Field()
    """
    The ID of the payment. Like all Plaid identifiers, the `payment_id` is case sensitive.
    """

    recipient_id: str = pydantic.Field()
    """
    The ID of the recipient
    """

    reference: str = pydantic.Field()
    """
    A reference for the payment.
    """

    refund_details: typing.Optional[ExternalPaymentRefundDetails] = None
    refund_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Refund IDs associated with the payment.
    """

    schedule: typing.Optional[ExternalPaymentScheduleGet] = None
    scheme: typing.Optional[PaymentScheme] = None
    status: PaymentInitiationPaymentStatus
    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts.
    """

    wallet_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
