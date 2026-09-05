

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetPodcastsInBatchForm(UniversalBaseModel):
    ids: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated list of podcast ids.
    """

    itunes_ids: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated Apple Podcasts (iTunes) ids, e.g., 659155419
    """

    next_episode_pub_date: typing.Optional[int] = pydantic.Field(default=None)
    """
    For latest episodes pagination. It's the value of **next_episode_pub_date** from the response of last request. If not specified, just return latest 15 episodes.
    """

    rsses: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated rss urls.
    """

    show_latest_episodes: typing.Optional[int] = pydantic.Field(default=None)
    """
    Whether or not to fetch up to 15 latest episodes from these podcasts, sorted by pub_date. 1 is yes, and 0 is no.
    """

    spotify_ids: typing.Optional[str] = pydantic.Field(default=None)
    """
    Comma-separated Spotify ids, e.g., 3DDfEsKDIDrTlnPOiG4ZF4
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
