

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_amount import TransferAmount
from .transfer_event_type import TransferEventType
from .transfer_failure import TransferFailure
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_id import TransferId
from .transfer_sweep_amount import TransferSweepAmount
from .transfer_sweep_id import TransferSweepId
from .transfer_type import TransferType


class TransferEvent(UniversalBaseModel):
    """
    Represents an event in the Transfers API.
    """

    account_id: str = pydantic.Field()
    """
    The account ID associated with the transfer.
    """

    event_id: int = pydantic.Field()
    """
    Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.
    """

    event_type: TransferEventType
    failure_reason: typing.Optional[TransferFailure] = None
    funding_account_id: TransferFundingAccountIdResponse
    origination_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the origination account that this balance belongs to.
    """

    originator_client_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid client ID that is the originator of the transfer that this event applies to. Only present if the transfer was created on behalf of another client as a third-party sender (TPS).
    """

    refund_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plaid’s unique identifier for a refund. A non-null value indicates the event is for the associated refund of the transfer.
    """

    sweep_amount: typing.Optional[TransferSweepAmount] = None
    sweep_id: typing.Optional[TransferSweepId] = None
    timestamp: dt.datetime = pydantic.Field()
    """
    The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.
    """

    transfer_amount: TransferAmount
    transfer_id: TransferId
    transfer_type: TransferType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
