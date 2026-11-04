

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_provider_spec_auth_type import AuthProviderSpecAuthType
from .config_map_ref import ConfigMapRef
from .setting_ref import SettingRef


class AuthProviderSpec(UniversalBaseModel):
    """
    Authentication provider metadata and endpoint configuration.
    """

    auth_type: typing_extensions.Annotated[
        AuthProviderSpecAuthType,
        FieldMetadata(alias="authType"),
        pydantic.Field(alias="authType", description="Auth type: form or oauth2."),
    ]
    """
    Auth type: form or oauth2.
    """

    authentication_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="authenticationUrl"),
        pydantic.Field(alias="authenticationUrl", description="URL that starts the authentication flow."),
    ]
    """
    URL that starts the authentication flow.
    """

    binding_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bindingUrl"),
        pydantic.Field(
            alias="bindingUrl", description="URL that starts account binding for an already signed-in user."
        ),
    ] = None
    """
    URL that starts account binding for an already signed-in user.
    """

    config_map_ref: typing_extensions.Annotated[
        typing.Optional[ConfigMapRef], FieldMetadata(alias="configMapRef"), pydantic.Field(alias="configMapRef")
    ] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable description of the provider.
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown on sign-in and account binding screens."),
    ]
    """
    Display name shown on sign-in and account binding screens.
    """

    help_page: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="helpPage"),
        pydantic.Field(alias="helpPage", description="Help page URL for users who need sign-in assistance."),
    ] = None
    """
    Help page URL for users who need sign-in assistance.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    Logo URL or attachment URI for the provider.
    """

    method: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP method used when starting the authentication flow.
    """

    remember_me_support: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="rememberMeSupport"),
        pydantic.Field(
            alias="rememberMeSupport", description="Whether the provider supports remember-me during sign-in."
        ),
    ] = None
    """
    Whether the provider supports remember-me during sign-in.
    """

    setting_ref: typing_extensions.Annotated[
        typing.Optional[SettingRef], FieldMetadata(alias="settingRef"), pydantic.Field(alias="settingRef")
    ] = None
    unbind_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="unbindUrl"),
        pydantic.Field(alias="unbindUrl", description="URL that unbinds the external account from the current user."),
    ] = None
    """
    URL that unbinds the external account from the current user.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provider website URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
