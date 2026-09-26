

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_auth_group_filter import OtoroshiAuthGroupFilter
from .otoroshi_auth_group_rights import OtoroshiAuthGroupRights
from .otoroshi_auth_ldap_auth_module_config_admin_password import OtoroshiAuthLdapAuthModuleConfigAdminPassword
from .otoroshi_auth_ldap_auth_module_config_admin_username import OtoroshiAuthLdapAuthModuleConfigAdminUsername
from .otoroshi_auth_ldap_auth_module_config_metadata_field import OtoroshiAuthLdapAuthModuleConfigMetadataField
from .otoroshi_auth_ldap_auth_module_config_type import OtoroshiAuthLdapAuthModuleConfigType
from .otoroshi_auth_ldap_auth_module_config_user_base import OtoroshiAuthLdapAuthModuleConfigUserBase
from .otoroshi_models_user_rights import OtoroshiModelsUserRights
from .otoroshi_utils_json_path_validator import OtoroshiUtilsJsonPathValidator


class OtoroshiAuthLdapAuthModuleConfig(UniversalBaseModel):
    """
    ???
    """

    type: typing.Optional[OtoroshiAuthLdapAuthModuleConfigType] = pydantic.Field(default=None)
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

    allow_empty_password: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowEmptyPassword"),
        pydantic.Field(alias="allowEmptyPassword", description="???"),
    ] = None
    """
    ???
    """

    group_filters: typing_extensions.Annotated[
        typing.Optional[typing.List[OtoroshiAuthGroupFilter]],
        FieldMetadata(alias="groupFilters"),
        pydantic.Field(alias="groupFilters", description="???"),
    ] = None
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

    server_urls: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="serverUrls"),
        pydantic.Field(alias="serverUrls", description="???"),
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

    basic_auth: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="basicAuth"), pydantic.Field(alias="basicAuth", description="???")
    ] = None
    """
    ???
    """

    search_base: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="searchBase"), pydantic.Field(alias="searchBase", description="???")
    ] = None
    """
    ???
    """

    group_rights: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, OtoroshiAuthGroupRights]],
        FieldMetadata(alias="groupRights"),
        pydantic.Field(alias="groupRights", description="???"),
    ] = None
    """
    ???
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
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

    metadata_field: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthLdapAuthModuleConfigMetadataField],
        FieldMetadata(alias="metadataField"),
        pydantic.Field(alias="metadataField", description="???"),
    ] = None
    """
    ???
    """

    search_filter: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="searchFilter"),
        pydantic.Field(alias="searchFilter", description="???"),
    ] = None
    """
    ???
    """

    admin_username: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthLdapAuthModuleConfigAdminUsername],
        FieldMetadata(alias="adminUsername"),
        pydantic.Field(alias="adminUsername", description="???"),
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

    extract_profile_filter: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="extractProfileFilter"),
        pydantic.Field(alias="extractProfileFilter", description="???"),
    ] = None
    """
    ???
    """

    user_base: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthLdapAuthModuleConfigUserBase],
        FieldMetadata(alias="userBase"),
        pydantic.Field(alias="userBase", description="???"),
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
    admin_password: typing_extensions.Annotated[
        typing.Optional[OtoroshiAuthLdapAuthModuleConfigAdminPassword],
        FieldMetadata(alias="adminPassword"),
        pydantic.Field(alias="adminPassword", description="???"),
    ] = None
    """
    ???
    """

    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    ???
    """

    extract_profile_filter_not: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="extractProfileFilterNot"),
        pydantic.Field(alias="extractProfileFilterNot", description="???"),
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

    extract_profile: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="extractProfile"),
        pydantic.Field(alias="extractProfile", description="???"),
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
