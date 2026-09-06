

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AudioMetaTags(UniversalBaseModel):
    """
    ID3 metadata tags pulled from the audio file on import. Only non-null tags will be returned in requests.
    """

    tag_album: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagAlbum"), pydantic.Field(alias="tagAlbum")
    ] = None
    tag_artist: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagArtist"), pydantic.Field(alias="tagArtist")
    ] = None
    tag_genre: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagGenre"), pydantic.Field(alias="tagGenre")
    ] = None
    tag_title: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagTitle"), pydantic.Field(alias="tagTitle")
    ] = None
    tag_series: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagSeries"), pydantic.Field(alias="tagSeries")
    ] = None
    tag_series_part: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagSeriesPart"), pydantic.Field(alias="tagSeriesPart")
    ] = None
    tag_track: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagTrack"), pydantic.Field(alias="tagTrack")
    ] = None
    tag_disc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagDisc"), pydantic.Field(alias="tagDisc")
    ] = None
    tag_subtitle: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagSubtitle"), pydantic.Field(alias="tagSubtitle")
    ] = None
    tag_album_artist: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagAlbumArtist"), pydantic.Field(alias="tagAlbumArtist")
    ] = None
    tag_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagDate"), pydantic.Field(alias="tagDate")
    ] = None
    tag_composer: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagComposer"), pydantic.Field(alias="tagComposer")
    ] = None
    tag_publisher: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagPublisher"), pydantic.Field(alias="tagPublisher")
    ] = None
    tag_comment: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagComment"), pydantic.Field(alias="tagComment")
    ] = None
    tag_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagDescription"), pydantic.Field(alias="tagDescription")
    ] = None
    tag_encoder: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagEncoder"), pydantic.Field(alias="tagEncoder")
    ] = None
    tag_encoded_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagEncodedBy"), pydantic.Field(alias="tagEncodedBy")
    ] = None
    tag_isbn: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagIsbn"), pydantic.Field(alias="tagIsbn")
    ] = None
    tag_language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagLanguage"), pydantic.Field(alias="tagLanguage")
    ] = None
    tag_asin: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagASIN"), pydantic.Field(alias="tagASIN")
    ] = None
    tag_overdrive_media_marker: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tagOverdriveMediaMarker"),
        pydantic.Field(alias="tagOverdriveMediaMarker"),
    ] = None
    tag_original_year: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagOriginalYear"), pydantic.Field(alias="tagOriginalYear")
    ] = None
    tag_release_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagReleaseCountry"), pydantic.Field(alias="tagReleaseCountry")
    ] = None
    tag_release_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagReleaseType"), pydantic.Field(alias="tagReleaseType")
    ] = None
    tag_release_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagReleaseStatus"), pydantic.Field(alias="tagReleaseStatus")
    ] = None
    tag_isrc: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="tagISRC"), pydantic.Field(alias="tagISRC")
    ] = None
    tag_music_brainz_track_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tagMusicBrainzTrackId"),
        pydantic.Field(alias="tagMusicBrainzTrackId"),
    ] = None
    tag_music_brainz_album_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tagMusicBrainzAlbumId"),
        pydantic.Field(alias="tagMusicBrainzAlbumId"),
    ] = None
    tag_music_brainz_album_artist_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tagMusicBrainzAlbumArtistId"),
        pydantic.Field(alias="tagMusicBrainzAlbumArtistId"),
    ] = None
    tag_music_brainz_artist_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tagMusicBrainzArtistId"),
        pydantic.Field(alias="tagMusicBrainzArtistId"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
