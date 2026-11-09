

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_data_nullable import AddressDataNullable


class IdentityMatchUser(UniversalBaseModel):
    """
    The user's legal name, phone number, email address and address used to perform fuzzy match.
    """

    address: typing.Optional[AddressDataNullable] = None
    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address.
    """

    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's full legal name.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567". Phone numbers provided in other formats will be parsed on a best-effort basis.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
