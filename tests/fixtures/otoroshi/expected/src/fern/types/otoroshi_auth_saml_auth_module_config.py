

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_auth_saml_auth_module_config_email_attribute_name import (
    OtoroshiAuthSamlAuthModuleConfigEmailAttributeName,
)
from .otoroshi_auth_saml_auth_module_config_single_logout_url import OtoroshiAuthSamlAuthModuleConfigSingleLogoutUrl
from .otoroshi_auth_saml_auth_module_config_type import OtoroshiAuthSamlAuthModuleConfigType
from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator


class OtoroshiAuthSamlAuthModuleConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiAuthSamlAuthModuleConfigType] = pydantic.Field(default=None)
    """
    the type of the module
    """

    desc: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    sso_protocol_binding: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="ssoProtocolBinding"),
        pydantic.Field(alias="ssoProtocolBinding"),
    ] = None
    client_side_session_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="clientSideSessionEnabled"),
        pydantic.Field(alias="clientSideSessionEnabled", description="???"),
    ] = None
    """
    ???
    """

    email_attribute_name: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthSamlAuthModuleConfigEmailAttributeName],
        FieldMetadata(alias="emailAttributeName"),
        pydantic.Field(alias="emailAttributeName", description="???"),
    ] = None
    """
    ???
    """

    validating_certificates: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="validatingCertificates"),
        pydantic.Field(alias="validatingCertificates", description="???"),
    ] = None
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    ???
    """

    single_logout_protocol_binding: typing_extensions.Annotated[
        typing.Optional[typing.Any],
        FieldMetadata(alias="singleLogoutProtocolBinding"),
        pydantic.Field(alias="singleLogoutProtocolBinding"),
    ] = None
    session_max_age: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sessionMaxAge"),
        pydantic.Field(alias="sessionMaxAge", description="???"),
    ] = None
    """
    ???
    """

    issuer: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    signature: typing.Optional[typing.Any] = None
    user_validators: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiUtilsJsonPathValidator]],
        FieldMetadata(alias="userValidators"),
        pydantic.Field(alias="userValidators", description="???"),
    ] = None
    """
    ???
    """

    single_logout_url: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthSamlAuthModuleConfigSingleLogoutUrl],
        FieldMetadata(alias="singleLogoutUrl"),
        pydantic.Field(alias="singleLogoutUrl", description="???"),
    ] = None
    """
    ???
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ???
    """

    loc: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="_loc"), pydantic.Field(alias="_loc")
    ] = None
    used_name_id_as_email: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="usedNameIDAsEmail"),
        pydantic.Field(alias="usedNameIDAsEmail", description="???"),
    ] = None
    """
    ???
    """

    single_sign_on_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="singleSignOnUrl"),
        pydantic.Field(alias="singleSignOnUrl", description="???"),
    ] = None
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    validate_assertions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="validateAssertions"),
        pydantic.Field(alias="validateAssertions", description="???"),
    ] = None
    """
    ???
    """

    name_id_format: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="nameIDFormat"), pydantic.Field(alias="nameIDFormat")
    ] = None
    validate_signature: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="validateSignature"),
        pydantic.Field(alias="validateSignature", description="???"),
    ] = None
    """
    ???
    """

    credentials: typing.Optional[typing.Any] = None
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
