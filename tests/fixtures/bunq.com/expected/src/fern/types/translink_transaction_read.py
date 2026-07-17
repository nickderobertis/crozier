

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .amount import Amount
from .error import Error
from .label_monetary_account import LabelMonetaryAccount
from .translink_transaction_entry import TranslinkTransactionEntry


class TranslinkTransactionRead(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount containing the public information of 'this' (party) side of the Payment.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount of the transaction.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the payment request.
    """

    entries: typing.Optional[typing.List[TranslinkTransactionEntry]] = pydantic.Field(default=None)
    """
    The list of entries in the transaction.
    """

    failure_reason: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The reason why the transaction FAILED processing.
    """

    payments: typing.Optional["PaymentBatchAnchoredPayment"] = pydantic.Field(default=None)
    """
    The list of mutations that were made.
    """

    reference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The request reference.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the transaction. Can be CREATED, SETTLED or FAILED.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of transaction, can be TRIP, REFUND, WITHDRAWAL or TOP_UP.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment
from .payment_auto_allocate_instance import PaymentAutoAllocateInstance
from .payment_batch import PaymentBatch
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    TranslinkTransactionRead,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
