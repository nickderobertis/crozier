

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .amount import Amount
from .request_inquiry import RequestInquiry
from .request_reference_split_the_bill_anchor_object import RequestReferenceSplitTheBillAnchorObject


class RequestInquiryBatchRead(UniversalBaseModel):
    reference_split_the_bill: typing.Optional[RequestReferenceSplitTheBillAnchorObject] = pydantic.Field(default=None)
    """
    The reference to the object used for split the bill. Can be Payment, PaymentBatch, ScheduleInstance, RequestResponse and MasterCardAction
    """

    request_inquiries: typing.Optional[typing.List[RequestInquiry]] = pydantic.Field(default=None)
    """
    The list of requests that were made.
    """

    total_amount_inquired: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount originally inquired for this batch.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(RequestInquiryBatchRead)
