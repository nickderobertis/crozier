

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_event_id import TransactionEventId
from .transaction_event_status import TransactionEventStatus
from .transaction_event_type import TransactionEventType
from .transaction_id import TransactionId


class ReceiptEvent(UniversalBaseModel):
    """
    Transaction event details as rendered on the receipt.
    """

    id: typing.Optional[TransactionEventId] = None
    transaction_id: typing.Optional[TransactionId] = None
    type: typing.Optional[TransactionEventType] = None
    status: typing.Optional[TransactionEventStatus] = None
    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    Amount associated with the transaction event, in major units.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the transaction event occurred.
    """

    receipt_no: typing.Optional[str] = pydantic.Field(default=None)
    """
    Receipt number associated with the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
