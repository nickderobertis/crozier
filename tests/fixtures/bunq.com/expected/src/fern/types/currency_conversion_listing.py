

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .amount import Amount
from .label_monetary_account import LabelMonetaryAccount


class CurrencyConversionListing(UniversalBaseModel):
    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the conversion.
    """

    counter_amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the counter conversion.
    """

    counter_label_monetary_account: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label of the counter monetary account.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the conversion's creation.
    """

    date_delivery_expected: typing.Optional[str] = pydantic.Field(default=None)
    """
    The expected delivery date of the conversion.
    """

    group_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The group uuid of the conversion.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the conversion.
    """

    label_monetary_account: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The label of the monetary account.
    """

    payment: typing.Optional["Payment"] = pydantic.Field(default=None)
    """
    The payment associated with this conversion.
    """

    rate: typing.Optional[str] = pydantic.Field(default=None)
    """
    The rate of the conversion.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the conversion.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of this conversion in the pair.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the conversion's last update.
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
    CurrencyConversionListing,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
