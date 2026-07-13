

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .co_owner import CoOwner
from .monetary_account_setting import MonetaryAccountSetting
from .pointer import Pointer


class MonetaryAccountJoint(UniversalBaseModel):
    alias: typing.Optional[typing.List[Pointer]] = pydantic.Field(default=None)
    """
    The Aliases to add to MonetaryAccountJoint. Must all be confirmed first. Can mostly be ignored.
    """

    all_co_owner: typing.List[CoOwner] = pydantic.Field()
    """
    The users the account will be joint with.
    """

    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID of the Avatar of the MonetaryAccountJoint.
    """

    currency: str = pydantic.Field()
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

    overdraft_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The maximum Amount the MonetaryAccountJoint can be 'in the red'. Must be 0 EUR or omitted.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for voluntarily cancelling (closing) the MonetaryAccountJoint, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    """

    reason_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountJoint. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    """

    setting: typing.Optional[MonetaryAccountSetting] = pydantic.Field(default=None)
    """
    The settings of the MonetaryAccountJoint.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the MonetaryAccountJoint. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountJoint. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the MonetaryAccountJoint providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
