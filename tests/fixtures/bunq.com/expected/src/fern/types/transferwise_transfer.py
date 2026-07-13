

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount
from .transferwise_quote import TransferwiseQuote


class TransferwiseTransfer(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    """

    amount_source: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The source amount.
    """

    amount_target: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The target amount.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of the other (counterparty) side of the Payment.
    """

    monetary_account_id: str = pydantic.Field()
    """
    The id of the monetary account the payment should be made from.
    """

    pay_in_reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Pay-In reference of the payment.
    """

    quote: typing.Optional[TransferwiseQuote] = pydantic.Field(default=None)
    """
    The quote details used to created the payment.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate of the payment.
    """

    recipient_id: str = pydantic.Field()
    """
    The id of the target account.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reference of the payment.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status.
    """

    status_transferwise: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status as Transferwise reports it.
    """

    status_transferwise_issue: typing.Optional[str] = pydantic.Field(default=None)
    """
    A status to indicatie if Transferwise has an issue with this payment and requires more information.
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subStatus.
    """

    time_delivery_estimate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The estimated delivery time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
