

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .branding import Branding
from .phone_number import PhoneNumber


class BusinessProfile(UniversalBaseModel):
    """
    Business information about the merchant. This information will be visible to the merchant's customers.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer-facing business name.
    """

    dynamic_descriptor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The descriptor is the text that your customer sees on their bank account statement.
    The more recognisable your descriptor is, the less risk you have of receiving disputes (e.g. chargebacks).
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    The business's publicly available website.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    A publicly available email address.
    """

    phone_number: typing.Optional[PhoneNumber] = None
    address: typing.Optional[Address] = None
    branding: typing.Optional[Branding] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
