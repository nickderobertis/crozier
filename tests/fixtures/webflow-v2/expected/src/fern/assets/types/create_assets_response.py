

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_assets_response_upload_details import CreateAssetsResponseUploadDetails


class CreateAssetsResponse(UniversalBaseModel):
    upload_details: typing_extensions.Annotated[
        typing.Optional[CreateAssetsResponseUploadDetails],
        FieldMetadata(alias="uploadDetails"),
        pydantic.Field(alias="uploadDetails", description="Metadata for uploading the asset binary"),
    ] = None
    """
    Metadata for uploading the asset binary
    """

    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    id: typing.Optional[str] = None
    parent_folder: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentFolder"),
        pydantic.Field(alias="parentFolder", description="Parent folder for the asset"),
    ] = None
    """
    Parent folder for the asset
    """

    upload_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uploadUrl"), pydantic.Field(alias="uploadUrl")
    ] = None
    asset_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="assetUrl"),
        pydantic.Field(alias="assetUrl", description="S3 link to the asset"),
    ] = None
    """
    S3 link to the asset
    """

    hosted_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hostedUrl"),
        pydantic.Field(alias="hostedUrl", description="Represents the link to the asset"),
    ] = None
    """
    Represents the link to the asset
    """

    original_file_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originalFileName"),
        pydantic.Field(
            alias="originalFileName",
            description="Original file name when uploaded. If not specified at time of upload, it may be extracted from the raw file name",
        ),
    ] = None
    """
    Original file name when uploaded. If not specified at time of upload, it may be extracted from the raw file name
    """

    created_on: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdOn"),
        pydantic.Field(alias="createdOn", description="Date the asset metadata was created"),
    ] = None
    """
    Date the asset metadata was created
    """

    last_updated: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastUpdated"),
        pydantic.Field(alias="lastUpdated", description="Date the asset metadata was last updated"),
    ] = None
    """
    Date the asset metadata was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
