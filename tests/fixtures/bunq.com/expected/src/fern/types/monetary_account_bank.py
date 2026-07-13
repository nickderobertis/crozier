

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .amount import Amount
from .monetary_account_setting import MonetaryAccountSetting


class MonetaryAccountBank(UniversalBaseModel):
    avatar_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The UUID of the Avatar of the MonetaryAccountBank.
    """

    country_iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the monetary account IBAN.
    """

    currency: str = pydantic.Field()
    """
    The currency of the MonetaryAccountBank as an ISO 4217 formatted currency code.
    """

    daily_limit: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The daily spending limit Amount of the MonetaryAccountBank. Defaults to 1000 EUR. Currency must match the MonetaryAccountBank's currency. Limited to 10000 EUR.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the MonetaryAccountBank. Defaults to 'bunq account'.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The legal name of the user / company using this monetary account.
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    The reason for voluntarily cancelling (closing) the MonetaryAccountBank, can only be OTHER. Should only be specified if updating the status to CANCELLED.
    """

    reason_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The optional free-form reason for voluntarily cancelling (closing) the MonetaryAccountBank. Can be any user provided message. Should only be specified if updating the status to CANCELLED.
    """

    setting: typing.Optional[MonetaryAccountSetting] = pydantic.Field(default=None)
    """
    The settings of the MonetaryAccountBank.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the MonetaryAccountBank. Ignored in POST requests (always set to ACTIVE) can be CANCELLED or PENDING_REOPEN in PUT requests to cancel (close) or reopen the MonetaryAccountBank. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    """

    sub_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sub-status of the MonetaryAccountBank providing extra information regarding the status. Should be ignored for POST requests. In case of PUT requests with status CANCELLED it can only be REDEMPTION_VOLUNTARY, while with status PENDING_REOPEN it can only be NONE. When updating the status and/or sub_status no other fields can be updated in the same request (and vice versa).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
