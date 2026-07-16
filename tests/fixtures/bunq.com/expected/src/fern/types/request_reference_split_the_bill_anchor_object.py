

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .draft_payment import DraftPayment
from .invoice import Invoice
from .master_card_action import MasterCardAction
from .request_response import RequestResponse
from .schedule_instance import ScheduleInstance
from .transferwise_transfer import TransferwiseTransfer
from .whitelist_result import WhitelistResult


class RequestReferenceSplitTheBillAnchorObject(UniversalBaseModel):
    billing_invoice: typing_extensions.Annotated[
        typing.Optional[Invoice],
        FieldMetadata(alias="BillingInvoice"),
        pydantic.Field(alias="BillingInvoice", description=""),
    ] = None
    """
    
    """

    draft_payment: typing_extensions.Annotated[
        typing.Optional[DraftPayment],
        FieldMetadata(alias="DraftPayment"),
        pydantic.Field(alias="DraftPayment", description=""),
    ] = None
    """
    
    """

    master_card_action: typing_extensions.Annotated[
        typing.Optional[MasterCardAction],
        FieldMetadata(alias="MasterCardAction"),
        pydantic.Field(alias="MasterCardAction", description=""),
    ] = None
    """
    
    """

    payment: typing_extensions.Annotated[
        typing.Optional["Payment"], FieldMetadata(alias="Payment"), pydantic.Field(alias="Payment", description="")
    ] = None
    """
    
    """

    payment_batch: typing_extensions.Annotated[
        typing.Optional["PaymentBatch"],
        FieldMetadata(alias="PaymentBatch"),
        pydantic.Field(alias="PaymentBatch", description=""),
    ] = None
    """
    
    """

    request_response: typing_extensions.Annotated[
        typing.Optional[RequestResponse],
        FieldMetadata(alias="RequestResponse"),
        pydantic.Field(alias="RequestResponse", description=""),
    ] = None
    """
    
    """

    schedule_instance: typing_extensions.Annotated[
        typing.Optional[ScheduleInstance],
        FieldMetadata(alias="ScheduleInstance"),
        pydantic.Field(alias="ScheduleInstance", description=""),
    ] = None
    """
    
    """

    transferwise_payment: typing_extensions.Annotated[
        typing.Optional[TransferwiseTransfer],
        FieldMetadata(alias="TransferwisePayment"),
        pydantic.Field(alias="TransferwisePayment", description=""),
    ] = None
    """
    
    """

    whitelist_result: typing_extensions.Annotated[
        typing.Optional[WhitelistResult],
        FieldMetadata(alias="WhitelistResult"),
        pydantic.Field(alias="WhitelistResult", description=""),
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
from .payment_batch_anchored_payment import PaymentBatchAnchoredPayment

update_forward_refs(
    RequestReferenceSplitTheBillAnchorObject,
    Payment=Payment,
    PaymentAutoAllocateInstance=PaymentAutoAllocateInstance,
    PaymentBatch=PaymentBatch,
    PaymentBatchAnchoredPayment=PaymentBatchAnchoredPayment,
)
