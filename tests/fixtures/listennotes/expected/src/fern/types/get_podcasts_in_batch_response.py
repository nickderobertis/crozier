

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .episode_simple import EpisodeSimple
from .podcast_simple import PodcastSimple


class GetPodcastsInBatchResponse(UniversalBaseModel):
    latest_episodes: typing.Optional[typing.List[EpisodeSimple]] = pydantic.Field(default=None)
    """
    Up to 10 latest episodes from these podcasts, sorted by **pub_date**. This field shows up only when **show_latest_episodes** is 1.
    """

    podcasts: typing.List[PodcastSimple]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
