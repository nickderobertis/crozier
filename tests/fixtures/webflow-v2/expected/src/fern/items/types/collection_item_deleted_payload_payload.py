

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .collection_item_deleted_payload_payload_field_data import CollectionItemDeletedPayloadPayloadFieldData


class CollectionItemDeletedPayloadPayload(UniversalBaseModel):
    """
    The payload of data sent from Webflow
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the collection item that was deleted
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="The ID of the site"),
    ] = None
    """
    The ID of the site
    """

    workspace_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workspaceId"),
        pydantic.Field(alias="workspaceId", description="The ID of the workspace"),
    ] = None
    """
    The ID of the workspace
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(alias="collectionId", description="The ID of the collection"),
    ] = None
    """
    The ID of the collection
    """

    cms_locale_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cmsLocaleId"),
        pydantic.Field(alias="cmsLocaleId", description="Unique identifier of the CMS locale for this item"),
    ] = None
    """
    Unique identifier of the CMS locale for this item
    """

    last_published: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastPublished"), pydantic.Field(alias="lastPublished")
    ] = None
    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ] = None
    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn")
    ] = None
    is_archived: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isArchived"), pydantic.Field(alias="isArchived")
    ] = None
    is_draft: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isDraft"), pydantic.Field(alias="isDraft")
    ] = None
    field_data: typing_extensions.Annotated[
        typing.Optional[CollectionItemDeletedPayloadPayloadFieldData],
        FieldMetadata(alias="fieldData"),
        pydantic.Field(alias="fieldData"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
