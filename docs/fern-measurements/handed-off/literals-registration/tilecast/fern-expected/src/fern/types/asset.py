

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_status import AssetStatus
from .asset_type import AssetType
from .asset_variant import AssetVariant
from .widget import Widget


class Asset(UniversalBaseModel):
    id: str
    name: str
    description: str
    type: AssetType
    original_filename: typing_extensions.Annotated[
        str, FieldMetadata(alias="originalFilename"), pydantic.Field(alias="originalFilename")
    ]
    declared_mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="declaredMimeType"), pydantic.Field(alias="declaredMimeType")
    ] = None
    detected_mime_type: typing_extensions.Annotated[
        str, FieldMetadata(alias="detectedMimeType"), pydantic.Field(alias="detectedMimeType")
    ]
    sha256: str
    original_size: typing_extensions.Annotated[
        int, FieldMetadata(alias="originalSize"), pydantic.Field(alias="originalSize")
    ]
    width: typing.Optional[int] = None
    height: typing.Optional[int] = None
    duration_seconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="durationSeconds"), pydantic.Field(alias="durationSeconds")
    ] = None
    frame_rate: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="frameRate"), pydantic.Field(alias="frameRate")
    ] = None
    video_codec: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="videoCodec"), pydantic.Field(alias="videoCodec")
    ] = None
    audio_codec: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="audioCodec"), pydantic.Field(alias="audioCodec")
    ] = None
    audio_channels: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="audioChannels"), pydantic.Field(alias="audioChannels")
    ] = None
    metadata: typing.Dict[str, typing.Any]
    processing_status: typing_extensions.Annotated[
        AssetStatus, FieldMetadata(alias="processingStatus"), pydantic.Field(alias="processingStatus")
    ]
    processing_progress: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="processingProgress"), pydantic.Field(alias="processingProgress")
    ] = None
    error_code: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorCode"), pydantic.Field(alias="errorCode")
    ] = None
    error_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="errorMessage"), pydantic.Field(alias="errorMessage")
    ] = None
    thumbnail_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="thumbnailUrl"), pydantic.Field(alias="thumbnailUrl")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    updated_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ]
    available_from: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="availableFrom"), pydantic.Field(alias="availableFrom")
    ] = None
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    archived_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="archivedAt"), pydantic.Field(alias="archivedAt")
    ] = None
    variants: typing.List[AssetVariant]
    widget: typing.Optional[Widget] = None
    playlist_usage: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="playlistUsage"), pydantic.Field(alias="playlistUsage")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
