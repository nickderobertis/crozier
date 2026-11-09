

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .recurring_transfer_id import RecurringTransferId
from .transfer_amount import TransferAmount
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_id import TransferId
from .transfer_network import TransferNetwork
from .transfer_recurring_schedule import TransferRecurringSchedule
from .transfer_recurring_status import TransferRecurringStatus
from .transfer_type import TransferType
from .transfer_user_in_response import TransferUserInResponse


class RecurringTransfer(UniversalBaseModel):
    """
    Represents a recurring transfer within the Transfers API.
    """

    account_id: str = pydantic.Field()
    """
    The Plaid `account_id` corresponding to the end-user account that will be debited or credited.
    """

    ach_class: typing.Optional[AchClass] = None
    amount: TransferAmount
    created: dt.datetime = pydantic.Field()
    """
    The datetime when this transfer was created. This will be of the form `2006-01-02T15:04:05Z`
    """

    description: str = pydantic.Field()
    """
    The description of the recurring transfer.
    """

    funding_account_id: TransferFundingAccountIdResponse
    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount, e.g. "USD"
    """

    network: TransferNetwork
    next_origination_date: dt.date = pydantic.Field()
    """
    A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    
    The next transfer origination date after bank holiday adjustment.
    """

    origination_account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the origination account that was used for this transfer.
    """

    recurring_transfer_id: RecurringTransferId
    schedule: TransferRecurringSchedule
    status: TransferRecurringStatus
    test_clock_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plaid’s unique identifier for a test clock.
    """

    transfer_ids: typing.List[TransferId]
    type: TransferType
    user: TransferUserInResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
