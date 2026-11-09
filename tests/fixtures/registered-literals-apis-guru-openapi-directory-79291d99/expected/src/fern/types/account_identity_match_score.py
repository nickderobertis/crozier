

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .account_base import AccountBase
from .address_match_score import AddressMatchScore
from .email_address_match_score import EmailAddressMatchScore
from .name_match_score import NameMatchScore
from .phone_number_match_score import PhoneNumberMatchScore


class AccountIdentityMatchScore(AccountBase):
    """
    Identity match scores for an account
    """

    address: typing.Optional[AddressMatchScore] = None
    email_address: typing.Optional[EmailAddressMatchScore] = None
    legal_name: typing.Optional[NameMatchScore] = None
    phone_number: typing.Optional[PhoneNumberMatchScore] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
