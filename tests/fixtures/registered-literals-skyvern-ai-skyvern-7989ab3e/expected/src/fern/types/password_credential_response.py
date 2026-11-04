

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .totp_type import TotpType


class PasswordCredentialResponse(UniversalBaseModel):
    """
    Response model for password credentials — non-sensitive fields only.

    SECURITY: Must NEVER include password or TOTP secret.
    """

    username: str = pydantic.Field()
    """
    The username associated with the credential
    """

    totp_type: typing.Optional[TotpType] = pydantic.Field(default=None)
    """
    Type of 2FA method used for this credential
    """

    totp_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifier (email or phone number) used to fetch TOTP codes
    """

    has_totp: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the stored password credential includes a non-empty TOTP seed. Legacy rows with an unknown value report false until the credential is updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
