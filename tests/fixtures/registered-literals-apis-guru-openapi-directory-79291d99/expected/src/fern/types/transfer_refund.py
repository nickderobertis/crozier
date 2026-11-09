

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_id_for_refund import TransferIdForRefund
from .transfer_refund_amount import TransferRefundAmount
from .transfer_refund_id import TransferRefundId
from .transfer_refund_status import TransferRefundStatus


class TransferRefund(UniversalBaseModel):
    """
    Represents a refund within the Transfers API.
    """

    amount: TransferRefundAmount
    created: dt.datetime = pydantic.Field()
    """
    The datetime when this refund was created. This will be of the form `2006-01-02T15:04:05Z`
    """

    id: TransferRefundId
    status: TransferRefundStatus
    transfer_id: TransferIdForRefund

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
