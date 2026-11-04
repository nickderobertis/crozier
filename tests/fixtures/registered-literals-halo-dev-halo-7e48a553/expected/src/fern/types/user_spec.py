

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UserSpec(UniversalBaseModel):
    """
    Desired user profile and authentication settings.
    """

    avatar: typing.Optional[str] = pydantic.Field(default=None)
    """
    Avatar URL or attachment URI for the user.
    """

    bio: typing.Optional[str] = pydantic.Field(default=None)
    """
    User biography shown on profile surfaces.
    """

    disabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user account is disabled.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the user."),
    ]
    """
    Display name shown for the user.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address used for sign-in and notifications.
    """

    email_verified: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="emailVerified"),
        pydantic.Field(alias="emailVerified", description="Whether the email address has been verified."),
    ] = None
    """
    Whether the email address has been verified.
    """

    login_history_limit: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loginHistoryLimit"),
        pydantic.Field(
            alias="loginHistoryLimit", description="Maximum number of login history entries retained for this user."
        ),
    ] = None
    """
    Maximum number of login history entries retained for this user.
    """

    password: typing.Optional[str] = pydantic.Field(default=None)
    """
    Password hash or encoded password value.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number associated with the user.
    """

    registered_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="registeredAt"),
        pydantic.Field(alias="registeredAt", description="Time when the user registered."),
    ] = None
    """
    Time when the user registered.
    """

    totp_encrypted_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totpEncryptedSecret"),
        pydantic.Field(
            alias="totpEncryptedSecret", description="Encrypted TOTP secret used for two-factor authentication."
        ),
    ] = None
    """
    Encrypted TOTP secret used for two-factor authentication.
    """

    two_factor_auth_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="twoFactorAuthEnabled"),
        pydantic.Field(
            alias="twoFactorAuthEnabled", description="Whether two-factor authentication is enabled for this user."
        ),
    ] = None
    """
    Whether two-factor authentication is enabled for this user.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
