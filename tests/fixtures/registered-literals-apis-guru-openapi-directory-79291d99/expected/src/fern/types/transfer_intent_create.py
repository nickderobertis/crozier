

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_class import AchClass
from .transfer_amount import TransferAmount
from .transfer_funding_account_id_response import TransferFundingAccountIdResponse
from .transfer_intent_create_mode import TransferIntentCreateMode
from .transfer_intent_create_network import TransferIntentCreateNetwork
from .transfer_intent_status import TransferIntentStatus
from .transfer_metadata import TransferMetadata
from .transfer_user_in_response import TransferUserInResponse


class TransferIntentCreate(UniversalBaseModel):
    """
    Represents a transfer intent within Transfer UI.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Plaid `account_id` corresponding to the end-user account that will be debited or credited. Returned only if `account_id` was set on intent creation.
    """

    ach_class: typing.Optional[AchClass] = None
    amount: TransferAmount
    created: dt.datetime = pydantic.Field()
    """
    The datetime the transfer was created. This will be of the form `2006-01-02T15:04:05Z`.
    """

    description: str = pydantic.Field()
    """
    A description for the underlying transfer. Maximum of 8 characters.
    """

    funding_account_id: TransferFundingAccountIdResponse
    id: str = pydantic.Field()
    """
    Plaid's unique identifier for the transfer intent object.
    """

    iso_currency_code: str = pydantic.Field()
    """
    The currency of the transfer amount, e.g. "USD"
    """

    metadata: typing.Optional[TransferMetadata] = None
    mode: TransferIntentCreateMode
    network: typing.Optional[TransferIntentCreateNetwork] = None
    origination_account_id: str = pydantic.Field()
    """
    Plaid’s unique identifier for the origination account for the intent. If not provided, the default account will be used.
    """

    require_guarantee: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When `true`, the transfer requires a `GUARANTEED` decision by Plaid to proceed (Guarantee customers only).
    """

    status: TransferIntentStatus
    user: TransferUserInResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
