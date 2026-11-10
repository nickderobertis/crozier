

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .client_user_id import ClientUserId
from .email_address import EmailAddress
from .identity_verification_request_user_name import IdentityVerificationRequestUserName
from .identity_verification_user_phone_number import IdentityVerificationUserPhoneNumber
from .iso8601date import Iso8601Date
from .user_address import UserAddress
from .user_id_number import UserIdNumber


class IdentityVerificationRequestUser(UniversalBaseModel):
    """
    User information collected outside of Link, most likely via your own onboarding process.

    Each of the following identity fields are optional:

    `email_address`

    `phone_number`

    `date_of_birth`

    `name`

    `address`

    `id_number`

    Specifically, these fields are optional in that they can either be fully provided (satisfying every required field in their subschema) or omitted from the request entirely by not providing the key or value.
    Providing these fields via the API will result in Link skipping the data collection process for the associated user. All verification steps enabled in the associated Identity Verification Template will still be run. Verification steps will either be run immediately, or once the user completes the `accept_tos` step, depending on the value provided to the `gave_consent` field.
    """

    address: typing.Optional[UserAddress] = None
    client_user_id: ClientUserId
    date_of_birth: typing.Optional[Iso8601Date] = None
    email_address: typing.Optional[EmailAddress] = None
    id_number: typing.Optional[UserIdNumber] = None
    name: typing.Optional[IdentityVerificationRequestUserName] = None
    phone_number: typing.Optional[IdentityVerificationUserPhoneNumber] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
