

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .book_cover_path import BookCoverPath
from .book_metadata_minified import BookMetadataMinified
from .duration_sec import DurationSec
from .size import Size
from .tags import Tags


class BookMinified(UniversalBaseModel):
    """
    Minified book schema. Does not depend on `bookBase` because there's pretty much no overlap.
    """

    metadata: typing.Optional[BookMetadataMinified] = None
    cover_path: typing_extensions.Annotated[
        typing.Optional[BookCoverPath], FieldMetadata(alias="coverPath"), pydantic.Field(alias="coverPath")
    ] = None
    tags: typing.Optional[Tags] = None
    num_tracks: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numTracks"),
        pydantic.Field(alias="numTracks", description="The number of tracks the book's audio files have."),
    ] = None
    """
    The number of tracks the book's audio files have.
    """

    num_audio_files: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numAudioFiles"),
        pydantic.Field(alias="numAudioFiles", description="The number of audio files the book has."),
    ] = None
    """
    The number of audio files the book has.
    """

    num_chapters: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numChapters"),
        pydantic.Field(alias="numChapters", description="The number of chapters the book has."),
    ] = None
    """
    The number of chapters the book has.
    """

    num_missing_parts: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numMissingParts"),
        pydantic.Field(alias="numMissingParts", description="The total number of missing parts the book has."),
    ] = None
    """
    The total number of missing parts the book has.
    """

    num_invalid_audio_files: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numInvalidAudioFiles"),
        pydantic.Field(alias="numInvalidAudioFiles", description="The number of invalid audio files the book has."),
    ] = None
    """
    The number of invalid audio files the book has.
    """

    duration: typing.Optional[DurationSec] = None
    size: typing.Optional[Size] = None
    ebook_format: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ebookFormat"),
        pydantic.Field(
            alias="ebookFormat",
            description="The format of ebook of the book. Will be null if the book is an audiobook.",
        ),
    ] = None
    """
    The format of ebook of the book. Will be null if the book is an audiobook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
