

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .signal_address_data import SignalAddressData
from .signal_person_name import SignalPersonName


class SignalUser(UniversalBaseModel):
    """
    Details about the end user initiating the transaction (i.e., the account holder).
    """

    address: typing.Optional[SignalAddressData] = None
    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address.
    """

    name: typing.Optional[SignalPersonName] = None
    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number, in E.164 format: +{countrycode}{number}. For example: "+14151234567"
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
