

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .email_address_nullable import EmailAddressNullable
from .identity_verification_response_user_name import IdentityVerificationResponseUserName
from .identity_verification_user_address import IdentityVerificationUserAddress
from .identity_verification_user_phone_number import IdentityVerificationUserPhoneNumber
from .ip_address import IpAddress
from .iso8601date_nullable import Iso8601DateNullable
from .user_id_number import UserIdNumber


class IdentityVerificationUserData(UniversalBaseModel):
    """
    The identity data that was either collected from the user or provided via API in order to perform an identity verification.
    """

    address: typing.Optional[IdentityVerificationUserAddress] = None
    date_of_birth: typing.Optional[Iso8601DateNullable] = None
    email_address: typing.Optional[EmailAddressNullable] = None
    id_number: typing.Optional[UserIdNumber] = None
    ip_address: typing.Optional[IpAddress] = None
    name: typing.Optional[IdentityVerificationResponseUserName] = None
    phone_number: typing.Optional[IdentityVerificationUserPhoneNumber] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
