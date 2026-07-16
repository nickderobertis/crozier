

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class PaymentBatch(UniversalBaseModel):
    payments: typing.Optional["PaymentBatchAnchoredPayment"] = pydantic.Field(default=None)
    """
    The list of mutations that were made.
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
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    PaymentBatch,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
