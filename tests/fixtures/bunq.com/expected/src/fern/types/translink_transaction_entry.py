

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .attachment_monetary_account_payment import AttachmentMonetaryAccountPayment
from .label_monetary_account import LabelMonetaryAccount


class TranslinkTransactionEntry(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of 'this' (party) side of the payment.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the payment.
    """

    attachment: typing.Optional[typing.List[AttachmentMonetaryAccountPayment]] = pydantic.Field(default=None)
    """
    The Attachments attached to the payment.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of the other (counterparty) side of the payment.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the payment. Maximum 140 characters for payments to external IBANs, 9000 characters for payments to only other bunq MonetaryAccounts.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the payment entry.
    """

    merchant_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional data to be included with the Payment specific to the merchant.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the payment entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
