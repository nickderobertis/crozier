

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .genre_ids_field import GenreIdsField
from .image_field import ImageField
from .listen_score_field import ListenScoreField
from .listen_score_global_rank_field import ListenScoreGlobalRankField
from .podcast_id_field import PodcastIdField
from .podcast_ln_url_field import PodcastLnUrlField
from .podcast_title_highlighted_field import PodcastTitleHighlightedField
from .podcast_title_original_field import PodcastTitleOriginalField
from .publisher_highlighted_field import PublisherHighlightedField
from .publisher_original_field import PublisherOriginalField
from .thumbnail_field import ThumbnailField


class EpisodeSearchResultPodcast(UniversalBaseModel):
    """
    The podcast that this episode belongs to.
    """

    genre_ids: typing.Optional[GenreIdsField] = None
    id: typing.Optional[PodcastIdField] = None
    image: typing.Optional[ImageField] = None
    listen_score: typing.Optional[ListenScoreField] = None
    listen_score_global_rank: typing.Optional[ListenScoreGlobalRankField] = None
    listennotes_url: typing.Optional[PodcastLnUrlField] = None
    publisher_highlighted: typing.Optional[PublisherHighlightedField] = None
    publisher_original: typing.Optional[PublisherOriginalField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title_highlighted: typing.Optional[PodcastTitleHighlightedField] = None
    title_original: typing.Optional[PodcastTitleOriginalField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
