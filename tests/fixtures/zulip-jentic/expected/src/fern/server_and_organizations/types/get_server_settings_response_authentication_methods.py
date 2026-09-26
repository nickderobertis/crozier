

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetServerSettingsResponseAuthenticationMethods(UniversalBaseModel):
    """
    Each key-value pair in the object indicates whether the authentication
    method is enabled on this server.

    **Changes**: Deprecated in Zulip 2.1.0, in favor of the more expressive
    `external_authentication_methods`.
    """

    password: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using password.
    """

    dev: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using development API key.
    """

    email: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using email.
    """

    ldap: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using LDAP.
    """

    remoteuser: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using REMOTE_USER.
    """

    github: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using their GitHub account.
    """

    azuread: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using their Microsoft Entra ID account.
    """

    gitlab: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using their GitLab account.
    
    **Changes**: New in Zulip 3.0 (feature level 1).
    """

    apple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using their Apple account.
    """

    google: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using their Google account.
    """

    saml: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the user can authenticate using SAML.
    """

    openid_connect: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="openid connect"),
        pydantic.Field(alias="openid connect", description="Whether the user can authenticate using OpenID Connect."),
    ] = None
    """
    Whether the user can authenticate using OpenID Connect.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
