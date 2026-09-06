

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_sites_response_sites_item_custom_domains_item import ListSitesResponseSitesItemCustomDomainsItem
from .list_sites_response_sites_item_data_collection_type import ListSitesResponseSitesItemDataCollectionType
from .list_sites_response_sites_item_locales import ListSitesResponseSitesItemLocales


class ListSitesResponseSitesItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the Site
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="Unique identifier for the Workspace"),
    ] = None
    """
    Unique identifier for the Workspace
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date the Site was created"),
    ] = None
    """
    Date the Site was created
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Name given to Site"),
    ] = None
    """
    Name given to Site
    """

    short_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortName"),
        pydantic.Field(alias="shortName", description="Slugified version of name"),
    ] = None
    """
    Slugified version of name
    """

    last_published: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastPublished"),
        pydantic.Field(alias="lastPublished", description="Date the Site was last published"),
    ] = None
    """
    Date the Site was last published
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date the Site was last updated"),
    ] = None
    """
    Date the Site was last updated
    """

    preview_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="previewUrl"),
        pydantic.Field(alias="previewUrl", description="URL of a generated image for the given Site"),
    ] = None
    """
    URL of a generated image for the given Site
    """

    time_zone: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeZone"),
        pydantic.Field(alias="timeZone", description="Site timezone set under Site Settings"),
    ] = None
    """
    Site timezone set under Site Settings
    """

    parent_folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentFolderId"),
        pydantic.Field(alias="parentFolderId", description="The ID of the parent folder the Site exists in"),
    ] = None
    """
    The ID of the parent folder the Site exists in
    """

    custom_domains: typing_extensions.Annotated[
        typing.Optional[typing.List[ListSitesResponseSitesItemCustomDomainsItem]],
        FieldMetadata(alias="customDomains"),
        pydantic.Field(alias="customDomains"),
    ] = None
    locales: typing.Optional[ListSitesResponseSitesItemLocales] = None
    data_collection_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dataCollectionEnabled"),
        pydantic.Field(
            alias="dataCollectionEnabled", description="Indicates if data collection is enabled for the site."
        ),
    ] = None
    """
    Indicates if data collection is enabled for the site.
    """

    data_collection_type: typing_extensions.Annotated[
        typing.Optional[ListSitesResponseSitesItemDataCollectionType],
        FieldMetadata(alias="dataCollectionType"),
        pydantic.Field(alias="dataCollectionType", description="The type of data collection enabled for the site."),
    ] = None
    """
    The type of data collection enabled for the site.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
