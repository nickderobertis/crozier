

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from .label_monetary_account import LabelMonetaryAccount


class SchedulePaymentEntry(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    """

    allow_bunqto: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not sending a bunq.to payment is allowed.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The Amount transferred by the Payment. Will be negative for outgoing Payments and positive for incoming Payments (relative to the MonetaryAccount indicated by monetary_account_id).
    """

    attachment: typing.Optional[typing.List[AttachmentMonetaryAccountPayment]] = pydantic.Field(default=None)
    """
    The Attachments attached to the Payment.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the Payment. Maximum 140 characters for Payments to external IBANs, 9000 characters for Payments to only other bunq MonetaryAccounts.
    """

    merchant_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional data included with the Payment specific to the merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
