

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class PaymentBatchAnchoredPayment(UniversalBaseModel):
    payment: typing_extensions.Annotated[
        typing.Optional[typing.List["Payment"]],
        FieldMetadata(alias="Payment"),
        pydantic.Field(alias="Payment", description=""),
    ] = None
    """
    
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

update_forward_refs(
    PaymentBatchAnchoredPayment,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
)
