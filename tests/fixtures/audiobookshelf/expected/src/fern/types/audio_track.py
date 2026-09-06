

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_metadata import FileMetadata


class AudioTrack(UniversalBaseModel):
    """
    Represents an audio track with various properties.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the audio track.
    """

    start_offset: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="startOffset"),
        pydantic.Field(alias="startOffset", description="The start offset of the audio track in seconds."),
    ] = None
    """
    The start offset of the audio track in seconds.
    """

    duration: typing.Optional[float] = pydantic.Field(default=None)
    """
    The duration of the audio track in seconds.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the audio track.
    """

    content_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contentUrl"),
        pydantic.Field(alias="contentUrl", description="The URL where the audio track content is located."),
    ] = None
    """
    The URL where the audio track content is located.
    """

    mime_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mimeType"),
        pydantic.Field(alias="mimeType", description="The MIME type of the audio track."),
    ] = None
    """
    The MIME type of the audio track.
    """

    codec: typing.Optional[str] = pydantic.Field(default=None)
    """
    The codec used for the audio track.
    """

    metadata: typing.Optional[FileMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
