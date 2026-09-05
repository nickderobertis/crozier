

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_field import AudioField
from .audio_length_sec_field import AudioLengthSecField
from .episode_id_field import EpisodeIdField
from .episode_image_field import EpisodeImageField
from .episode_ln_url_field import EpisodeLnUrlField
from .episode_pub_date_ms_field import EpisodePubDateMsField
from .episode_search_result_podcast import EpisodeSearchResultPodcast
from .episode_thumbnail_field import EpisodeThumbnailField
from .explicit_field import ExplicitField
from .i_tunes_id_field import ITunesIdField
from .link_field import LinkField
from .rss_field import RssField


class EpisodeSearchResult(UniversalBaseModel):
    """
    When **type** is *episode*.
    """

    audio: typing.Optional[AudioField] = None
    audio_length_sec: typing.Optional[AudioLengthSecField] = None
    description_highlighted: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highlighted segment of this episode's description
    """

    description_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text of this episode's description
    """

    explicit_content: typing.Optional[ExplicitField] = None
    id: typing.Optional[EpisodeIdField] = None
    image: typing.Optional[EpisodeImageField] = None
    itunes_id: typing.Optional[ITunesIdField] = None
    link: typing.Optional[LinkField] = None
    listennotes_url: typing.Optional[EpisodeLnUrlField] = None
    podcast: typing.Optional[EpisodeSearchResultPodcast] = pydantic.Field(default=None)
    """
    The podcast that this episode belongs to.
    """

    pub_date_ms: typing.Optional[EpisodePubDateMsField] = None
    rss: typing.Optional[RssField] = None
    thumbnail: typing.Optional[EpisodeThumbnailField] = None
    title_highlighted: typing.Optional[str] = pydantic.Field(default=None)
    """
    Highlighted segment of this episode's title
    """

    title_original: typing.Optional[str] = pydantic.Field(default=None)
    """
    Plain text of this episode' title
    """

    transcripts_highlighted: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Up to 2 highlighted segments of the audio transcript of this episode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
