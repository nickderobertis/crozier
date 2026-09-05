

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_field import ImageField
from .podcast_id_field import PodcastIdField
from .podcast_ln_url_field import PodcastLnUrlField
from .podcast_name_field import PodcastNameField
from .publisher_field import PublisherField
from .rss_field import RssField
from .thumbnail_field import ThumbnailField


class PodcastMinimumRss(UniversalBaseModel):
    id: typing.Optional[PodcastIdField] = None
    image: typing.Optional[ImageField] = None
    listennotes_url: typing.Optional[PodcastLnUrlField] = None
    publisher: typing.Optional[PublisherField] = None
    rss: typing.Optional[RssField] = None
    thumbnail: typing.Optional[ThumbnailField] = None
    title: typing.Optional[PodcastNameField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
