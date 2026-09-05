

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .avg_audio_length_sec_field import AvgAudioLengthSecField
from .country_field import CountryField
from .earliest_pub_date_ms_field import EarliestPubDateMsField
from .email_field import EmailField
from .episode_minimum import EpisodeMinimum
from .explicit_field import ExplicitField
from .genre_ids_field import GenreIdsField
from .i_tunes_id_field import ITunesIdField
from .image_field import ImageField
from .is_claimed_field import IsClaimedField
from .language_field import LanguageField
from .latest_episode_id_field import LatestEpisodeIdField
from .latest_pub_date_ms_field import LatestPubDateMsField
from .listen_score_field import ListenScoreField
from .listen_score_global_rank_field import ListenScoreGlobalRankField
from .next_episode_pub_date_field import NextEpisodePubDateField
from .podcast_description_field import PodcastDescriptionField
from .podcast_extra_field import PodcastExtraField
from .podcast_id_field import PodcastIdField
from .podcast_ln_url_field import PodcastLnUrlField
from .podcast_looking_for_field import PodcastLookingForField
from .podcast_name_field import PodcastNameField
from .podcast_type_field import PodcastTypeField
from .publisher_field import PublisherField
from .rss_field import RssField
from .thumbnail_field import ThumbnailField
from .total_episodes_field import TotalEpisodesField
from .update_frequency_hours_field import UpdateFrequencyHoursField
from .website_field import WebsiteField


class PodcastFull(UniversalBaseModel):
    audio_length_sec: typing.Optional[AvgAudioLengthSecField] = None
    country: typing.Optional[CountryField] = None
    description: typing.Optional[PodcastDescriptionField] = None
    earliest_pub_date_ms: typing.Optional[EarliestPubDateMsField] = None
    email: typing.Optional[EmailField] = None
    episodes: typing.Optional[typing.List[EpisodeMinimum]] = None
    explicit_content: typing.Optional[ExplicitField] = None
    extra: typing.Optional[PodcastExtraField] = None
    genre_ids: typing.Optional[GenreIdsField] = None
    id: typing.Optional[PodcastIdField] = None
    image: typing.Optional[ImageField] = None
    is_claimed: typing.Optional[IsClaimedField] = None
    itunes_id: typing.Optional[ITunesIdField] = None
    language: typing.Optional[LanguageField] = None
    latest_episode_id: typing.Optional[LatestEpisodeIdField] = None
    latest_pub_date_ms: typing.Optional[LatestPubDateMsField] = None
    listen_score: typing.Optional[ListenScoreField] = None
    listen_score_global_rank: typing.Optional[ListenScoreGlobalRankField] = None
    listennotes_url: typing.Optional[PodcastLnUrlField] = None
    looking_for: typing.Optional[PodcastLookingForField] = None
    next_episode_pub_date: typing.Optional[NextEpisodePubDateField] = None
    publisher: typing.Optional[PublisherField] = None
    rss: typing.Optional[RssField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title: typing.Optional[PodcastNameField] = None
    total_episodes: typing.Optional[TotalEpisodesField] = None
    type: typing.Optional[PodcastTypeField] = None
    update_frequency_hours: typing.Optional[UpdateFrequencyHoursField] = None
    website: typing.Optional[WebsiteField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
