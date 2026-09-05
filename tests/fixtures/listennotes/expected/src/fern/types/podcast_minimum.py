

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_field import ImageField
from .listen_score_field import ListenScoreField
from .listen_score_global_rank_field import ListenScoreGlobalRankField
from .podcast_id_field import PodcastIdField
from .podcast_ln_url_field import PodcastLnUrlField
from .podcast_name_field import PodcastNameField
from .publisher_field import PublisherField
from .thumbnail_field import ThumbnailField


class PodcastMinimum(UniversalBaseModel):
    id: typing.Optional[PodcastIdField] = None
    image: typing.Optional[ImageField] = None
    listen_score: typing.Optional[ListenScoreField] = None
    listen_score_global_rank: typing.Optional[ListenScoreGlobalRankField] = None
    listennotes_url: typing.Optional[PodcastLnUrlField] = None
    publisher: typing.Optional[PublisherField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title: typing.Optional[PodcastNameField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
