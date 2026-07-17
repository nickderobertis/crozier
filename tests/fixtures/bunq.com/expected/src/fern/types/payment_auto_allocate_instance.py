

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .error import Error


class PaymentAutoAllocateInstance(UniversalBaseModel):
    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocateInstance was created.
    """

    error_message: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The error message, if the payment auto allocating failed.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the PaymentAutoAllocateInstance.
    """

    payment_auto_allocate_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the payment auto allocate this instance belongs to.
    """

    payment_batch: typing.Optional["PaymentBatch"] = pydantic.Field(default=None)
    """
    The payment batch allocating all the payments.
    """

    payment_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The ID of the payment that triggered the allocating of the payments.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the payment auto allocate instance. SUCCEEDED or FAILED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the PaymentAutoAllocateInstance was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .payment import Payment
from .payment_batch import PaymentBatch
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    PaymentAutoAllocateInstance,
    Payment=Payment,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
