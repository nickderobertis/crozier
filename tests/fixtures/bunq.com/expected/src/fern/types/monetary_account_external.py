

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .avatar import Avatar
from .bunq_id import BunqId
from .monetary_account_profile import MonetaryAccountProfile
from .monetary_account_setting import MonetaryAccountSetting
from .pointer import Pointer


class MonetaryAccountExternal(UniversalBaseModel):
    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The Aliases for the MonetaryAccountExternal.
    """

    all_auto_save_id: typing.Optional[typing.List[BunqId]] = pydantic.Field(default=None)
    """
    The ids of the AutoSave.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The Avatar of the MonetaryAccountExternal.
    """

    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID of the Avatar of the MonetaryAccountExternal.
    """

    balance: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The current available balance Amount of the MonetaryAccountExternal.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountExternal's creation.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the MonetaryAccountExternal as an ISO 4217 formatted currency code.
    """

    daily_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The daily spending limit Amount of the MonetaryAccountExternal. Defaults to 1000 EUR. Currency must match the MonetaryAccountExternal's currency. Limited to 10000 EUR.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the MonetaryAccountExternal. Defaults to 'bunq account'.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The legal name of the user / company using this monetary account.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccountExternal.
    """

    monetary_account_profile: typing.Optional[MonetaryAccountProfile] = pydantic.Field(default=None)
    """
    The profile of the account.
    """

    overdraft_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum Amount the MonetaryAccountExternal can be 'in the red'.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MonetaryAccountExternal's public UUID.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for voluntarily cancelling (closing) the MonetaryAccountExternal, can only be OTHER.
    """

    reason_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountExternal. Can be any user provided message.
    """

    setting: typing.Optional[MonetaryAccountSetting] = pydantic.Field(default=None)
    """
    The settings of the MonetaryAccountExternal.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the MonetaryAccountExternal. Can be: ACTIVE, BLOCKED, CANCELLED or PENDING_REOPEN
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the MonetaryAccountExternal providing extra information regarding the status. Will be NONE for ACTIVE or PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountExternal's last update.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the User who owns the MonetaryAccountExternal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
