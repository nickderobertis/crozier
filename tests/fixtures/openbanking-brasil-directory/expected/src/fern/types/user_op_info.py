

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UserOpInfo(UniversalBaseModel):
    """
    The information contained within is subject to the scopes passed during token generation
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address
    """

    email_verified: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the email verified
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family name
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Given name
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number
    """

    phone_number_verified: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the phone number verified
    """

    sub: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contains the email address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
