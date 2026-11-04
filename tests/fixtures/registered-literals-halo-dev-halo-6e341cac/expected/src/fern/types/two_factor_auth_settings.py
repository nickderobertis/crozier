

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TwoFactorAuthSettings(UniversalBaseModel):
    """
    Two-factor authentication settings for the current user.
    """

    available: bool = pydantic.Field()
    """
    Check if 2FA is available.
    """

    email_verified: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="emailVerified"),
        pydantic.Field(alias="emailVerified", description="Whether the user's email address has been verified."),
    ]
    """
    Whether the user's email address has been verified.
    """

    enabled: bool = pydantic.Field()
    """
    Whether two-factor authentication is enabled for the user.
    """

    totp_configured: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="totpConfigured"),
        pydantic.Field(alias="totpConfigured", description="Whether a TOTP authenticator has been configured."),
    ]
    """
    Whether a TOTP authenticator has been configured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
