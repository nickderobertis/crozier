

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .bank_transfer_amount import BankTransferAmount
from .bank_transfer_direction import BankTransferDirection
from .bank_transfer_failure import BankTransferFailure
from .bank_transfer_id import BankTransferId
from .bank_transfer_metadata import BankTransferMetadata
from .bank_transfer_network import BankTransferNetwork
from .bank_transfer_status import BankTransferStatus
from .bank_transfer_type import BankTransferType
from .bank_transfer_user import BankTransferUser


class BankTransfer(UniversalBaseModel):
    """
    Represents a bank transfer within the Bank Transfers API.
    """

    account_id: str = pydantic.Field()
    """
    The account ID that should be credited/debited for this bank transfer.
    """

    ach_class: AchClass
    amount: BankTransferAmount
    cancellable: bool = pydantic.Field()
    """
    When `true`, you can still cancel this bank transfer.
    """

    created: dt.datetime = pydantic.Field()
    """
    The datetime when this bank transfer was created. This will be of the form `2006-01-02T15:04:05Z`
    """

    custom_tag: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string containing the custom tag provided by the client in the create request. Will be null if not provided.
    """

    description: str = pydantic.Field()
    """
    The description of the transfer.
    """

    direction: typing.Optional[BankTransferDirection] = None
    failure_reason: typing.Optional[BankTransferFailure] = None
    id: BankTransferId
    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount, e.g. "USD"
    """

    metadata: typing.Optional[BankTransferMetadata] = None
    network: BankTransferNetwork
    origination_account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the origination account that was used for this transfer.
    """

    status: BankTransferStatus
    type: BankTransferType
    user: BankTransferUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
