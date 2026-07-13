

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .avatar import Avatar
from .monetary_account_setting import MonetaryAccountSetting
from .pointer import Pointer


class MonetaryAccountLight(UniversalBaseModel):
    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The Aliases for the MonetaryAccountLight.
    """

    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The Avatar of the MonetaryAccountLight.
    """

    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID of the Avatar of the MonetaryAccountLight.
    """

    balance: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The current available balance Amount of the MonetaryAccountLight.
    """

    balance_maximum: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum balance Amount of the MonetaryAccountLight.
    """

    budget_month_maximum: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount of the monthly budget.
    """

    budget_month_used: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the monthly budget used.
    """

    budget_withdrawal_year_maximum: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount of the yearly withdrawal budget.
    """

    budget_withdrawal_year_used: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the yearly withdrawal budget used.
    """

    budget_year_maximum: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The total amount of the yearly budget.
    """

    budget_year_used: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount of the yearly budget used.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountLight's creation.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency of the MonetaryAccountLight as an ISO 4217 formatted currency code.
    """

    daily_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The daily spending limit Amount of the MonetaryAccountLight. Defaults to 1000 EUR. Currency must match the MonetaryAccountLight's currency. Limited to 10000 EUR.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the MonetaryAccountLight. Defaults to 'bunq account'.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccountLight.
    """

    public_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The MonetaryAccountLight's public UUID.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER.
    """

    reason_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message.
    """

    setting: typing.Optional[MonetaryAccountSetting] = pydantic.Field(default=None)
    """
    The settings of the MonetaryAccountLight.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the MonetaryAccountLight. Can be: ACTIVE, BLOCKED, CANCELLED or PENDING_REOPEN
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the MonetaryAccountLight providing extra information regarding the status. Will be NONE for ACTIVE or PENDING_REOPEN, COMPLETELY or ONLY_ACCEPTING_INCOMING for BLOCKED and REDEMPTION_INVOLUNTARY, REDEMPTION_VOLUNTARY or PERMANENT for CANCELLED.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the MonetaryAccountLight's last update.
    """

    user_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the User who owns the MonetaryAccountLight.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
