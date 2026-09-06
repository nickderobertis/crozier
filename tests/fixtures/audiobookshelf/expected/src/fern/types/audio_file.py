

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .audio_meta_tags import AudioMetaTags
from .book_chapter import BookChapter
from .duration_sec import DurationSec
from .file_metadata import FileMetadata
from .inode import Inode
from .updated_at import UpdatedAt


class AudioFile(UniversalBaseModel):
    """
    An audio file for a book. Includes audio metadata and track numbers.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the audio file.
    """

    ino: typing.Optional[Inode] = None
    metadata: typing.Optional[FileMetadata] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    track_num_from_meta: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="trackNumFromMeta"),
        pydantic.Field(
            alias="trackNumFromMeta",
            description="The track number of the audio file as pulled from the file's metadata. Will be null if unknown.",
        ),
    ] = None
    """
    The track number of the audio file as pulled from the file's metadata. Will be null if unknown.
    """

    disc_num_from_meta: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="discNumFromMeta"),
        pydantic.Field(
            alias="discNumFromMeta",
            description="The disc number of the audio file as pulled from the file's metadata. Will be null if unknown.",
        ),
    ] = None
    """
    The disc number of the audio file as pulled from the file's metadata. Will be null if unknown.
    """

    track_num_from_filename: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="trackNumFromFilename"),
        pydantic.Field(
            alias="trackNumFromFilename",
            description="The track number of the audio file as determined from the file's name. Will be null if unknown.",
        ),
    ] = None
    """
    The track number of the audio file as determined from the file's name. Will be null if unknown.
    """

    disc_num_from_filename: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="discNumFromFilename"),
        pydantic.Field(
            alias="discNumFromFilename",
            description="The disc number of the audio file as determined from the file's name. Will be null if unknown.",
        ),
    ] = None
    """
    The disc number of the audio file as determined from the file's name. Will be null if unknown.
    """

    manually_verified: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="manuallyVerified"),
        pydantic.Field(
            alias="manuallyVerified", description="Whether the audio file has been manually verified by a user."
        ),
    ] = None
    """
    Whether the audio file has been manually verified by a user.
    """

    invalid: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the audio file is missing from the server.
    """

    exclude: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the audio file has been marked for exclusion.
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Any error with the audio file. Will be null if there is none.
    """

    format: typing.Optional[str] = pydantic.Field(default=None)
    """
    The format of the audio file.
    """

    duration: typing.Optional[DurationSec] = None
    bit_rate: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="bitRate"),
        pydantic.Field(alias="bitRate", description="The bit rate (in bit/s) of the audio file."),
    ] = None
    """
    The bit rate (in bit/s) of the audio file.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language of the audio file.
    """

    codec: typing.Optional[str] = pydantic.Field(default=None)
    """
    The codec of the audio file.
    """

    time_base: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="timeBase"),
        pydantic.Field(alias="timeBase", description="The time base of the audio file."),
    ] = None
    """
    The time base of the audio file.
    """

    channels: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of channels the audio file has.
    """

    channel_layout: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="channelLayout"),
        pydantic.Field(alias="channelLayout", description="The layout of the audio file's channels."),
    ] = None
    """
    The layout of the audio file's channels.
    """

    chapters: typing.Optional[typing.List[BookChapter]] = pydantic.Field(default=None)
    """
    If the audio file is part of an audiobook, the chapters the file contains.
    """

    embedded_cover_art: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="embeddedCoverArt"),
        pydantic.Field(
            alias="embeddedCoverArt",
            description="The type of embedded cover art in the audio file. Will be null if none exists.",
        ),
    ] = None
    """
    The type of embedded cover art in the audio file. Will be null if none exists.
    """

    meta_tags: typing_extensions.Annotated[
        typing.Optional[AudioMetaTags], FieldMetadata(alias="metaTags"), pydantic.Field(alias="metaTags")
    ] = None
    mime_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mimeType"),
        pydantic.Field(alias="mimeType", description="The MIME type of the audio file."),
    ] = None
    """
    The MIME type of the audio file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
