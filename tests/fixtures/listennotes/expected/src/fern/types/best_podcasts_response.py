

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .best_podcasts_ln_url_field import BestPodcastsLnUrlField
from .podcast_simple import PodcastSimple


class BestPodcastsResponse(UniversalBaseModel):
    has_next: bool
    has_previous: bool
    id: int = pydantic.Field()
    """
    The id of this genre
    """

    listennotes_url: BestPodcastsLnUrlField
    name: str = pydantic.Field()
    """
    This genre's name.
    """

    next_page_number: int
    page_number: int
    parent_id: int = pydantic.Field()
    """
    The id of parent genre.
    """

    podcasts: typing.List[PodcastSimple]
    previous_page_number: int
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
