

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_assets_response_assets_item_variants_item import ListAssetsResponseAssetsItemVariantsItem


class ListAssetsResponseAssetsItem(UniversalBaseModel):
    """
    Asset details
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for this asset
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentType"),
        pydantic.Field(alias="contentType", description="File format type"),
    ] = None
    """
    File format type
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    size in bytes
    """

    site_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="siteId"),
        pydantic.Field(alias="siteId", description="Unique identifier for the site that hosts this asset"),
    ] = None
    """
    Unique identifier for the site that hosts this asset
    """

    hosted_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hostedUrl"),
        pydantic.Field(alias="hostedUrl", description="Link to the asset"),
    ] = None
    """
    Link to the asset
    """

    original_file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originalFileName"),
        pydantic.Field(alias="originalFileName", description="Original file name at the time of upload"),
    ] = None
    """
    Original file name at the time of upload
    """

    display_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name of the asset"),
    ]
    """
    Display name of the asset
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date the asset metadata was last updated"),
    ] = None
    """
    Date the asset metadata was last updated
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date the asset metadata was created"),
    ] = None
    """
    Date the asset metadata was created
    """

    variants: typing.List[ListAssetsResponseAssetsItemVariantsItem] = pydantic.Field()
    """
    A list of [asset variants](https://help.webflow.com/hc/en-us/articles/33961378697107-Responsive-images) created by Webflow to serve your site responsively.
    """

    alt_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="altText"),
        pydantic.Field(alias="altText", description="The visual description of the asset"),
    ] = None
    """
    The visual description of the asset
    """

    folder_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="folderId"),
        pydantic.Field(
            alias="folderId",
            description="The ID of the folder the asset belongs to, or `null` if the asset is at the site root.\nThis field is present only in list responses (`GET /sites/{site_id}/assets`).",
        ),
    ] = None
    """
    The ID of the folder the asset belongs to, or `null` if the asset is at the site root.
    This field is present only in list responses (`GET /sites/{site_id}/assets`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
