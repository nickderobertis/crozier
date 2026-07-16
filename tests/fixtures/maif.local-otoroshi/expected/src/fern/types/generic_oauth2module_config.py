

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .generic_oauth2module_config_jwt_verifier import GenericOauth2ModuleConfigJwtVerifier


class GenericOauth2ModuleConfig(UniversalBaseModel):
    """
    Settings to authenticate users using a generic OAuth2 provider
    """

    access_token_field: typing_extensions.Annotated[str, FieldMetadata(alias="accessTokenField")] = pydantic.Field()
    """
    Field name to get access token
    """

    authorize_url: typing_extensions.Annotated[str, FieldMetadata(alias="authorizeUrl")] = pydantic.Field()
    """
    OAuth authorize URL
    """

    callback_url: typing_extensions.Annotated[str, FieldMetadata(alias="callbackUrl")] = pydantic.Field()
    """
    Otoroshi callback URL
    """

    claims: typing.Optional[str] = pydantic.Field(default=None)
    """
    The claims of the token
    """

    client_id: typing_extensions.Annotated[str, FieldMetadata(alias="clientId")] = pydantic.Field()
    """
    OAuth Client id
    """

    client_secret: typing_extensions.Annotated[str, FieldMetadata(alias="clientSecret")] = pydantic.Field()
    """
    OAuth Client secret
    """

    desc: str = pydantic.Field()
    """
    Description of the config
    """

    email_field: typing_extensions.Annotated[str, FieldMetadata(alias="emailField")] = pydantic.Field()
    """
    Field name to get email from user profile
    """

    id: str = pydantic.Field()
    """
    Unique id of the config
    """

    jwt_verifier: typing_extensions.Annotated[
        typing.Optional[GenericOauth2ModuleConfigJwtVerifier], FieldMetadata(alias="jwtVerifier")
    ] = pydantic.Field(default=None)
    """
    Algo. settings to verify JWT token
    """

    login_url: typing_extensions.Annotated[str, FieldMetadata(alias="loginUrl")] = pydantic.Field()
    """
    OAuth login URL
    """

    logout_url: typing_extensions.Annotated[str, FieldMetadata(alias="logoutUrl")] = pydantic.Field()
    """
    OAuth logout URL
    """

    name: str = pydantic.Field()
    """
    Name of the config
    """

    name_field: typing_extensions.Annotated[str, FieldMetadata(alias="nameField")] = pydantic.Field()
    """
    Field name to get name from user profile
    """

    oid_config: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="oidConfig")] = pydantic.Field(
        default=None
    )
    """
    URL of the OIDC config. file
    """

    otoroshi_data_field: typing_extensions.Annotated[str, FieldMetadata(alias="otoroshiDataField")] = pydantic.Field()
    """
    Field name to get otoroshi metadata from. You can specify sub fields using | as separator
    """

    read_profile_from_token: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="readProfileFromToken")
    ] = pydantic.Field(default=None)
    """
    The user profile will be read from the JWT token in id_token
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    The scope of the token
    """

    session_max_age: typing_extensions.Annotated[int, FieldMetadata(alias="sessionMaxAge")] = pydantic.Field()
    """
    Max age of the session
    """

    token_url: typing_extensions.Annotated[str, FieldMetadata(alias="tokenUrl")] = pydantic.Field()
    """
    OAuth token URL
    """

    type: str = pydantic.Field()
    """
    Type of settings. value is oauth2
    """

    use_cookies: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="useCookies")] = pydantic.Field(
        default=None
    )
    """
    Use for redirection to actual service
    """

    use_json: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="useJson")] = pydantic.Field(
        default=None
    )
    """
    Use JSON or URL Form Encoded as payload with the OAuth provider
    """

    user_info_url: typing_extensions.Annotated[str, FieldMetadata(alias="userInfoUrl")] = pydantic.Field()
    """
    OAuth userinfo to get user profile
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
