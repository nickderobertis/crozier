

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .avg_audio_length_sec_field import AvgAudioLengthSecField
from .earliest_pub_date_ms_field import EarliestPubDateMsField
from .email_field import EmailField
from .explicit_field import ExplicitField
from .genre_ids_field import GenreIdsField
from .i_tunes_id_field import ITunesIdField
from .image_field import ImageField
from .latest_episode_id_field import LatestEpisodeIdField
from .latest_pub_date_ms_field import LatestPubDateMsField
from .listen_score_field import ListenScoreField
from .listen_score_global_rank_field import ListenScoreGlobalRankField
from .podcast_id_field import PodcastIdField
from .podcast_ln_url_field import PodcastLnUrlField
from .podcast_title_highlighted_field import PodcastTitleHighlightedField
from .podcast_title_original_field import PodcastTitleOriginalField
from .publisher_highlighted_field import PublisherHighlightedField
from .publisher_original_field import PublisherOriginalField
from .rss_field import RssField
from .thumbnail_field import ThumbnailField
from .total_episodes_field import TotalEpisodesField
from .update_frequency_hours_field import UpdateFrequencyHoursField
from .website_field import WebsiteField


class PodcastSearchResult(UniversalBaseModel):
    """
    When **type** is *podcast*.
    """

    audio_length_sec: typing.Optional[AvgAudioLengthSecField] = None
    description_highlighted: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highlighted segment of podcast description
    """

    description_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text of podcast description
    """

    earliest_pub_date_ms: typing.Optional[EarliestPubDateMsField] = None
    email: typing.Optional[EmailField] = None
    explicit_content: typing.Optional[ExplicitField] = None
    genre_ids: typing.Optional[GenreIdsField] = None
    id: typing.Optional[PodcastIdField] = None
    image: typing.Optional[ImageField] = None
    itunes_id: typing.Optional[ITunesIdField] = None
    latest_episode_id: typing.Optional[LatestEpisodeIdField] = None
    latest_pub_date_ms: typing.Optional[LatestPubDateMsField] = None
    listen_score: typing.Optional[ListenScoreField] = None
    listen_score_global_rank: typing.Optional[ListenScoreGlobalRankField] = None
    listennotes_url: typing.Optional[PodcastLnUrlField] = None
    publisher_highlighted: typing.Optional[PublisherHighlightedField] = None
    publisher_original: typing.Optional[PublisherOriginalField] = None
    rss: typing.Optional[RssField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title_highlighted: typing.Optional[PodcastTitleHighlightedField] = None
    title_original: typing.Optional[PodcastTitleOriginalField] = None
    total_episodes: typing.Optional[TotalEpisodesField] = None
    update_frequency_hours: typing.Optional[UpdateFrequencyHoursField] = None
    website: typing.Optional[WebsiteField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
