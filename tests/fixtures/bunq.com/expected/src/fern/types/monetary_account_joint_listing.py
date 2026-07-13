

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .avatar import Avatar
from .bunq_id import BunqId
from .co_owner import CoOwner
from .monetary_account_profile import MonetaryAccountProfile
from .monetary_account_setting import MonetaryAccountSetting
from .pointer import Pointer


class MonetaryAccountJointListing(UniversalBaseModel):
    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The Aliases for the MonetaryAccountJoint.
    """

    all_auto_save_id: typing.Optional[typing.List[BunqId]] = pydantic.Field(default=None)
    """
    The ids of the AutoSave.
    """

    all_co_owner: typing.Optional[typing.List[CoOwner]] = pydantic.Field(default=None)
    """
    The users the account will be joint with.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The Avatar of the MonetaryAccountJoint.
    """

    balance: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The current available balance Amount of the MonetaryAccountJoint.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountJoint's creation.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the MonetaryAccountJoint as an ISO 4217 formatted currency code.
    """

    daily_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The daily spending limit Amount of the MonetaryAccountJoint. Defaults to 1000 EUR. Currency must match the MonetaryAccountJoint's currency. Limited to 10000 EUR.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the MonetaryAccountJoint. Defaults to 'bunq account'.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccountJoint.
    """

    monetary_account_profile: typing.Optional[MonetaryAccountProfile] = pydantic.Field(default=None)
    """
    The profile of the account.
    """

    overdraft_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum Amount the MonetaryAccountJoint can be 'in the red'.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MonetaryAccountJoint's public UUID.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER.
    """

    reason_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message.
    """

    setting: typing.Optional[MonetaryAccountSetting] = pydantic.Field(default=None)
    """
    The settings of the MonetaryAccountJoint.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the MonetaryAccountJoint. Can be: ACTIVE, BLOCKED, CANCELLED or PENDING_REOPEN
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Will be NONE for ACTIVE or PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountJoint's last update.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the User who owns the MonetaryAccountJoint.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
