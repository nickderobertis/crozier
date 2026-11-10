

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_transfer_direction import BankTransferDirection
from .bank_transfer_event_type import BankTransferEventType
from .bank_transfer_failure import BankTransferFailure
from .bank_transfer_id import BankTransferId
from .bank_transfer_type import BankTransferType


class BankTransferEvent(UniversalBaseModel):
    """
    Represents an event in the Bank Transfers API.
    """

    account_id: str = pydantic.Field()
    """
    The account ID associated with the bank transfer.
    """

    bank_transfer_amount: str = pydantic.Field()
    """
    The bank transfer amount.
    """

    bank_transfer_id: BankTransferId
    bank_transfer_iso_currency_code: str = pydantic.Field()
    """
    The currency of the bank transfer amount.
    """

    bank_transfer_type: BankTransferType
    direction: typing.Optional[BankTransferDirection] = None
    event_id: int = pydantic.Field()
    """
    Plaid’s unique identifier for this event. IDs are sequential unsigned 64-bit integers.
    """

    event_type: BankTransferEventType
    failure_reason: typing.Optional[BankTransferFailure] = None
    origination_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the origination account that this balance belongs to.
    """

    timestamp: dt.datetime = pydantic.Field()
    """
    The datetime when this event occurred. This will be of the form `2006-01-02T15:04:05Z`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
