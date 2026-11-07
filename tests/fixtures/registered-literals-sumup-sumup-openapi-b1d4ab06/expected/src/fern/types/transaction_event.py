

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_event_id import TransactionEventId
from .transaction_event_status import TransactionEventStatus
from .transaction_event_type import TransactionEventType


class TransactionEvent(UniversalBaseModel):
    """
    Detailed information about a transaction event.
    """

    id: typing.Optional[TransactionEventId] = None
    event_type: typing.Optional[TransactionEventType] = None
    status: typing.Optional[TransactionEventStatus] = None
    amount: typing.Optional[float] = pydantic.Field(default=None)
    """
    Amount of the event.
    """

    due_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date when the transaction event is due to occur.
    """

    date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date when the transaction event occurred.
    """

    installment_number: typing.Optional[int] = pydantic.Field(default=None)
    """
    Consecutive number of the installment that is paid. Applicable only payout events, i.e. `event_type = PAYOUT`.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date and time of the transaction event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
