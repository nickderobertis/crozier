

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provisioning_api_user_details_backend_capabilities import ProvisioningApiUserDetailsBackendCapabilities
from .provisioning_api_user_details_quota import ProvisioningApiUserDetailsQuota


class ProvisioningApiUserDetails(UniversalBaseModel):
    additional_mail: typing.List[str]
    additional_mail_scope: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="additional_mailScope"),
        pydantic.Field(alias="additional_mailScope"),
    ] = None
    address: str
    address_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="addressScope"), pydantic.Field(alias="addressScope")
    ] = None
    avatar_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="avatarScope"), pydantic.Field(alias="avatarScope")
    ] = None
    backend: str
    backend_capabilities: typing_extensions.Annotated[
        ProvisioningApiUserDetailsBackendCapabilities,
        FieldMetadata(alias="backendCapabilities"),
        pydantic.Field(alias="backendCapabilities"),
    ]
    biography: str
    biography_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="biographyScope"), pydantic.Field(alias="biographyScope")
    ] = None
    displayname: str
    display_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="display-name"), pydantic.Field(alias="display-name")
    ]
    displayname_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displaynameScope"), pydantic.Field(alias="displaynameScope")
    ] = None
    email: typing.Optional[str] = None
    email_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="emailScope"), pydantic.Field(alias="emailScope")
    ] = None
    enabled: typing.Optional[bool] = None
    fediverse: typing.Optional[str] = None
    fediverse_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="fediverseScope"), pydantic.Field(alias="fediverseScope")
    ] = None
    groups: typing.List[str]
    headline: str
    headline_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="headlineScope"), pydantic.Field(alias="headlineScope")
    ] = None
    id: str
    language: str
    last_login: typing_extensions.Annotated[int, FieldMetadata(alias="lastLogin"), pydantic.Field(alias="lastLogin")]
    locale: str
    notify_email: typing.Optional[str] = None
    organisation: str
    organisation_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="organisationScope"), pydantic.Field(alias="organisationScope")
    ] = None
    phone: str
    phone_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="phoneScope"), pydantic.Field(alias="phoneScope")
    ] = None
    profile_enabled: str
    profile_enabled_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="profile_enabledScope"), pydantic.Field(alias="profile_enabledScope")
    ] = None
    quota: ProvisioningApiUserDetailsQuota
    role: str
    role_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="roleScope"), pydantic.Field(alias="roleScope")
    ] = None
    storage_location: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="storageLocation"), pydantic.Field(alias="storageLocation")
    ] = None
    subadmin: typing.List[str]
    twitter: str
    twitter_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="twitterScope"), pydantic.Field(alias="twitterScope")
    ] = None
    website: str
    website_scope: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="websiteScope"), pydantic.Field(alias="websiteScope")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
