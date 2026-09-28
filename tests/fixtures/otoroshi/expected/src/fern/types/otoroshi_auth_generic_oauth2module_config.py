

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_auth_generic_oauth2module_config_jwt_verifier import OtoroshiAuthGenericOauth2ModuleConfigJwtVerifier
from .otoroshi_auth_generic_oauth2module_config_oid_config import OtoroshiAuthGenericOauth2ModuleConfigOidConfig
from .otoroshi_auth_generic_oauth2module_config_pkce import OtoroshiAuthGenericOauth2ModuleConfigPkce
from .otoroshi_auth_generic_oauth2module_config_proxy import OtoroshiAuthGenericOauth2ModuleConfigProxy
from .otoroshi_auth_generic_oauth2module_config_type import OtoroshiAuthGenericOauth2ModuleConfigType
from .otoroshi_models_user_rights import OtoroshiModelsUserRights
from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator


class OtoroshiAuthGenericOauth2ModuleConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiAuthGenericOauth2ModuleConfigType] = pydantic.Field(default=None)
    """
    the type of the module
    """

    extra_metadata: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="extraMetadata"),
        pydantic.Field(alias="extraMetadata", description="???"),
    ] = None
    """
    ???
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    rights_override: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, OtoroshiModelsUserRights]],
        FieldMetadata(alias="rightsOverride"),
        pydantic.Field(alias="rightsOverride", description="???"),
    ] = None
    """
    ???
    """

    client_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="clientId"), pydantic.Field(alias="clientId", description="???")
    ] = None
    """
    ???
    """

    otoroshi_rights_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="otoroshiRightsField"),
        pydantic.Field(alias="otoroshiRightsField", description="???"),
    ] = None
    """
    ???
    """

    client_side_session_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="clientSideSessionEnabled"),
        pydantic.Field(alias="clientSideSessionEnabled", description="???"),
    ] = None
    """
    ???
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    access_token_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accessTokenField"),
        pydantic.Field(alias="accessTokenField", description="???"),
    ] = None
    """
    ???
    """

    super_admins: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="superAdmins"),
        pydantic.Field(alias="superAdmins", description="???"),
    ] = None
    """
    ???
    """

    session_max_age: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sessionMaxAge"),
        pydantic.Field(alias="sessionMaxAge", description="???"),
    ] = None
    """
    ???
    """

    refresh_tokens: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="refreshTokens"),
        pydantic.Field(alias="refreshTokens", description="???"),
    ] = None
    """
    ???
    """

    login_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="loginUrl"), pydantic.Field(alias="loginUrl", description="???")
    ] = None
    """
    ???
    """

    api_key_tags_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyTagsField"),
        pydantic.Field(alias="apiKeyTagsField", description="???"),
    ] = None
    """
    ???
    """

    otoroshi_data_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="otoroshiDataField"),
        pydantic.Field(alias="otoroshiDataField", description="???"),
    ] = None
    """
    ???
    """

    user_validators: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiUtilsJsonPathValidator]],
        FieldMetadata(alias="userValidators"),
        pydantic.Field(alias="userValidators", description="???"),
    ] = None
    """
    ???
    """

    email_field: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="emailField"), pydantic.Field(alias="emailField", description="???")
    ] = None
    """
    ???
    """

    mtls_config: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="mtlsConfig"), pydantic.Field(alias="mtlsConfig")
    ] = None
    token_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tokenUrl"), pydantic.Field(alias="tokenUrl", description="???")
    ] = None
    """
    ???
    """

    use_cookie: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useCookie"), pydantic.Field(alias="useCookie", description="???")
    ] = None
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    pkce: typing.Optional[OtoroshiAuthGenericOauth2ModuleConfigPkce] = pydantic.Field(default=None)
    """
    ???
    """

    authorize_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="authorizeUrl"),
        pydantic.Field(alias="authorizeUrl", description="???"),
    ] = None
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    callback_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callbackUrl"), pydantic.Field(alias="callbackUrl", description="???")
    ] = None
    """
    ???
    """

    proxy: typing.Optional[OtoroshiAuthGenericOauth2ModuleConfigProxy] = pydantic.Field(default=None)
    """
    ???
    """

    api_key_meta_field: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="apiKeyMetaField"),
        pydantic.Field(alias="apiKeyMetaField", description="???"),
    ] = None
    """
    ???
    """

    client_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientSecret"),
        pydantic.Field(alias="clientSecret", description="???"),
    ] = None
    """
    ???
    """

    use_json: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="useJson"), pydantic.Field(alias="useJson", description="???")
    ] = None
    """
    ???
    """

    oid_config: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthGenericOauth2ModuleConfigOidConfig],
        FieldMetadata(alias="oidConfig"),
        pydantic.Field(alias="oidConfig", description="???"),
    ] = None
    """
    ???
    """

    claims: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    no_wildcard_redirect_uri: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="noWildcardRedirectURI"),
        pydantic.Field(alias="noWildcardRedirectURI", description="???"),
    ] = None
    """
    ???
    """

    name_field: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nameField"), pydantic.Field(alias="nameField", description="???")
    ] = None
    """
    ???
    """

    introspection_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="introspectionUrl"),
        pydantic.Field(alias="introspectionUrl", description="???"),
    ] = None
    """
    ???
    """

    logout_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logoutUrl"), pydantic.Field(alias="logoutUrl", description="???")
    ] = None
    """
    ???
    """

    data_override: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="dataOverride"),
        pydantic.Field(alias="dataOverride", description="???"),
    ] = None
    """
    ???
    """

    user_info_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userInfoUrl"), pydantic.Field(alias="userInfoUrl", description="???")
    ] = None
    """
    ???
    """

    jwt_verifier: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthGenericOauth2ModuleConfigJwtVerifier],
        FieldMetadata(alias="jwtVerifier"),
        pydantic.Field(alias="jwtVerifier", description="???"),
    ] = None
    """
    ???
    """

    read_profile_from_token: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="readProfileFromToken"),
        pydantic.Field(alias="readProfileFromToken", description="???"),
    ] = None
    """
    ???
    """

    session_cookie_values: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="sessionCookieValues"),
        pydantic.Field(alias="sessionCookieValues"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
