

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cloud_resource_model_additional_info import CloudResourceModelAdditionalInfo
from .cloud_resource_model_cloud_type import CloudResourceModelCloudType


class CloudResourceModel(UniversalBaseModel):
    """
    Model for Cloud Resource
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Account
    """

    account_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountId"),
        pydantic.Field(alias="accountId", description="Account ID"),
    ] = None
    """
    Account ID
    """

    additional_info: typing_extensions.Annotated[
        typing.Optional[CloudResourceModelAdditionalInfo],
        FieldMetadata(alias="additionalInfo"),
        pydantic.Field(alias="additionalInfo", description="Additional info"),
    ] = None
    """
    Additional info
    """

    cloud_account_ancestors: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="cloudAccountAncestors"),
        pydantic.Field(alias="cloudAccountAncestors", description="Cloud account ancestors. For GCP."),
    ] = None
    """
    Cloud account ancestors. For GCP.
    """

    cloud_account_groups: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="cloudAccountGroups"),
        pydantic.Field(alias="cloudAccountGroups", description="Cloud account groups"),
    ] = None
    """
    Cloud account groups
    """

    cloud_account_owners: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="cloudAccountOwners"),
        pydantic.Field(alias="cloudAccountOwners", description="Cloud account owners. For Azure and GCP."),
    ] = None
    """
    Cloud account owners. For Azure and GCP.
    """

    cloud_service_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cloudServiceName"),
        pydantic.Field(alias="cloudServiceName", description="Cloud service name"),
    ] = None
    """
    Cloud service name
    """

    cloud_type: typing_extensions.Annotated[
        typing.Optional[CloudResourceModelCloudType],
        FieldMetadata(alias="cloudType"),
        pydantic.Field(alias="cloudType", description="Cloud type"),
    ] = None
    """
    Cloud type
    """

    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Raw JSON data for the resource
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Id
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Region name
    """

    region_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="regionId"),
        pydantic.Field(alias="regionId", description="Region API identifier"),
    ] = None
    """
    Region API identifier
    """

    resource_api_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceApiName"),
        pydantic.Field(alias="resourceApiName", description="Resource API name"),
    ] = None
    """
    Resource API name
    """

    resource_config_json_available: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="resourceConfigJsonAvailable"),
        pydantic.Field(alias="resourceConfigJsonAvailable"),
    ] = None
    resource_details_available: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="resourceDetailsAvailable"),
        pydantic.Field(alias="resourceDetailsAvailable"),
    ] = None
    resource_tags: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="resourceTags"),
        pydantic.Field(alias="resourceTags", description="Resource tags"),
    ] = None
    """
    Resource tags
    """

    resource_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="resourceType"),
        pydantic.Field(alias="resourceType", description="Resource type"),
    ] = None
    """
    Resource type
    """

    rrn: typing.Optional[str] = pydantic.Field(default=None)
    """
    RRN
    """

    unified_asset_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="unifiedAssetId"), pydantic.Field(alias="unifiedAssetId")
    ] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
