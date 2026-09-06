

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auto_download_episodes import AutoDownloadEpisodes
from .library_item_id import LibraryItemId
from .podcast_episode import PodcastEpisode
from .podcast_id import PodcastId
from .podcast_metadata import PodcastMetadata


class Podcast(UniversalBaseModel):
    """
    A podcast containing multiple episodes.
    """

    id: typing.Optional[PodcastId] = None
    library_item_id: typing_extensions.Annotated[
        typing.Optional[LibraryItemId], FieldMetadata(alias="libraryItemId"), pydantic.Field(alias="libraryItemId")
    ] = None
    metadata: typing.Optional[PodcastMetadata] = None
    cover_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="coverPath"),
        pydantic.Field(alias="coverPath", description="The file path to the podcast's cover image."),
    ] = None
    """
    The file path to the podcast's cover image.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The tags associated with the podcast.
    """

    episodes: typing.Optional[typing.List[PodcastEpisode]] = pydantic.Field(default=None)
    """
    The episodes of the podcast.
    """

    auto_download_episodes: typing_extensions.Annotated[
        typing.Optional[AutoDownloadEpisodes],
        FieldMetadata(alias="autoDownloadEpisodes"),
        pydantic.Field(alias="autoDownloadEpisodes"),
    ] = None
    auto_download_schedule: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="autoDownloadSchedule"),
        pydantic.Field(
            alias="autoDownloadSchedule", description="The schedule for automatic episode downloads, in cron format."
        ),
    ] = None
    """
    The schedule for automatic episode downloads, in cron format.
    """

    last_episode_check: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastEpisodeCheck"),
        pydantic.Field(alias="lastEpisodeCheck", description="The timestamp of the last episode check."),
    ] = None
    """
    The timestamp of the last episode check.
    """

    max_episodes_to_keep: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxEpisodesToKeep"),
        pydantic.Field(alias="maxEpisodesToKeep", description="The maximum number of episodes to keep."),
    ] = None
    """
    The maximum number of episodes to keep.
    """

    max_new_episodes_to_download: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxNewEpisodesToDownload"),
        pydantic.Field(
            alias="maxNewEpisodesToDownload",
            description="The maximum number of new episodes to download when automatically downloading epsiodes.",
        ),
    ] = None
    """
    The maximum number of new episodes to download when automatically downloading epsiodes.
    """

    last_cover_search: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="lastCoverSearch"),
        pydantic.Field(alias="lastCoverSearch", description="The timestamp of the last cover search."),
    ] = None
    """
    The timestamp of the last cover search.
    """

    last_cover_search_query: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="lastCoverSearchQuery"),
        pydantic.Field(alias="lastCoverSearchQuery", description="The query used for the last cover search."),
    ] = None
    """
    The query used for the last cover search.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total size of all episodes in bytes.
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total duration of all episodes in seconds.
    """

    num_tracks: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="numTracks"),
        pydantic.Field(alias="numTracks", description="The number of tracks (episodes) in the podcast."),
    ] = None
    """
    The number of tracks (episodes) in the podcast.
    """

    latest_episode_published: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="latestEpisodePublished"),
        pydantic.Field(
            alias="latestEpisodePublished", description="The timestamp of the most recently published episode."
        ),
    ] = None
    """
    The timestamp of the most recently published episode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
