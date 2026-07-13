

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .amount import Amount
from .attachment import Attachment
from .geolocation import Geolocation
from .label_monetary_account import LabelMonetaryAccount


class TokenQrRequestIdealCreate(UniversalBaseModel):
    address_billing: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The billing address provided by the accepting user if an address was requested.
    """

    address_shipping: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The shipping address provided by the accepting user if an address was requested.
    """

    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the MonetaryAccount this RequestResponse was received on.
    """

    amount_inquired: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The requested Amount.
    """

    amount_responded: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The Amount the RequestResponse was accepted with.
    """

    attachment: typing.Optional[typing.List[Attachment]] = pydantic.Field(default=None)
    """
    The Attachments attached to the RequestResponse.
    """

    counterparty_alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the MonetaryAccount that is requesting money with this RequestResponse.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the RequestResponse provided by the requesting party. Maximum 9000 characters.
    """

    eligible_whitelist_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The whitelist id for this action or null.
    """

    geolocation: typing.Optional[Geolocation] = pydantic.Field(default=None)
    """
    The Geolocation where the RequestResponse was created.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the RequestResponse.
    """

    minimum_age: typing.Optional[int] = pydantic.Field(default=None)
    """
    The minimum age the user accepting the RequestResponse must have.
    """

    monetary_account_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the MonetaryAccount the RequestResponse was received on.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL which the user is sent to after accepting or rejecting the Request.
    """

    require_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether or not an address must be provided on accept.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the created RequestResponse. Can only be PENDING.
    """

    sub_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subtype of the RequestResponse. Can be only be NONE.
    """

    time_expiry: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the RequestResponse expired or will expire.
    """

    time_responded: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the RequestResponse was responded to.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the RequestResponse. Can be only be IDEAL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
