

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .added_at import AddedAt
from .audio_file import AudioFile
from .audio_track import AudioTrack
from .created_at import CreatedAt
from .duration_sec import DurationSec
from .library_item_id import LibraryItemId
from .old_podcast_id import OldPodcastId
from .podcast_id import PodcastId
from .size import Size
from .updated_at import UpdatedAt


class PodcastEpisode(UniversalBaseModel):
    """
    A single episode of a podcast.
    """

    library_item_id: typing_extensions.Annotated[
        typing.Optional[LibraryItemId], FieldMetadata(alias="libraryItemId"), pydantic.Field(alias="libraryItemId")
    ] = None
    podcast_id: typing_extensions.Annotated[
        typing.Optional[PodcastId], FieldMetadata(alias="podcastId"), pydantic.Field(alias="podcastId")
    ] = None
    id: typing.Optional[PodcastId] = None
    old_episode_id: typing_extensions.Annotated[
        typing.Optional[OldPodcastId], FieldMetadata(alias="oldEpisodeId"), pydantic.Field(alias="oldEpisodeId")
    ] = None
    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the episode within the podcast.
    """

    season: typing.Optional[str] = pydantic.Field(default=None)
    """
    The season number of the episode.
    """

    episode: typing.Optional[str] = pydantic.Field(default=None)
    """
    The episode number within the season.
    """

    episode_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="episodeType"),
        pydantic.Field(alias="episodeType", description="The type of episode (e.g., full, trailer)."),
    ] = None
    """
    The type of episode (e.g., full, trailer).
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the episode.
    """

    subtitle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The subtitle of the episode.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the episode.
    """

    enclosure: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The enclosure object containing additional episode data.
    """

    guid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The globally unique identifier for the episode.
    """

    pub_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pubDate"),
        pydantic.Field(alias="pubDate", description="The publication date of the episode."),
    ] = None
    """
    The publication date of the episode.
    """

    chapters: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = pydantic.Field(default=None)
    """
    The chapters within the episode.
    """

    audio_file: typing_extensions.Annotated[
        typing.Optional[AudioFile], FieldMetadata(alias="audioFile"), pydantic.Field(alias="audioFile")
    ] = None
    published_at: typing_extensions.Annotated[
        typing.Optional[CreatedAt], FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ] = None
    added_at: typing_extensions.Annotated[
        typing.Optional[AddedAt], FieldMetadata(alias="addedAt"), pydantic.Field(alias="addedAt")
    ] = None
    updated_at: typing_extensions.Annotated[
        typing.Optional[UpdatedAt], FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")
    ] = None
    audio_track: typing_extensions.Annotated[
        typing.Optional[AudioTrack], FieldMetadata(alias="audioTrack"), pydantic.Field(alias="audioTrack")
    ] = None
    duration: typing.Optional[DurationSec] = None
    size: typing.Optional[Size] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
