

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TrackMetadataMetaData(UniversalBaseModel):
    album: typing.Optional[str] = pydantic.Field(default=None)
    """
    Album name
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Track title
    """

    subtitle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Subtitle
    """

    artist: typing.Optional[str] = pydantic.Field(default=None)
    """
    Artist name
    """

    album_art_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="albumArtURI"),
        pydantic.Field(alias="albumArtURI", description="URL to the album art"),
    ] = None
    """
    URL to the album art
    """

    sample_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sampleRate"),
        pydantic.Field(alias="sampleRate", description="Sample rate in Hz"),
    ] = None
    """
    Sample rate in Hz
    """

    bit_depth: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bitDepth"),
        pydantic.Field(alias="bitDepth", description="Bit depth in bits"),
    ] = None
    """
    Bit depth in bits
    """

    bit_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="bitRate"),
        pydantic.Field(alias="bitRate", description="Bit rate in kbps"),
    ] = None
    """
    Bit rate in kbps
    """

    track_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="trackId"), pydantic.Field(alias="trackId", description="Track ID")
    ] = None
    """
    Track ID
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
