

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_event_id import TransactionEventId
from .transaction_event_status import TransactionEventStatus
from .transaction_event_type import TransactionEventType
from .transaction_id import TransactionId


class Event(UniversalBaseModel):
    """
    High-level transaction event details.
    """

    id: typing.Optional[TransactionEventId] = None
    transaction_id: typing.Optional[TransactionId] = None
    type: typing.Optional[TransactionEventType] = None
    status: typing.Optional[TransactionEventStatus] = None
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount associated with the transaction event, in major units.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The timestamp of when the transaction event occurred.
    """

    fee_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Fee associated with the transaction event, in major units.
    """

    installment_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Consecutive number of the installment associated with the event.
    """

    deducted_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount deducted from the merchant for the event, in major units.
    """

    deducted_fee_amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Fee deducted from the merchant for the event, in major units.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
