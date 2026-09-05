

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PodcastExtraField(UniversalBaseModel):
    amazon_music_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Amazon Music url for this podcast
    """

    facebook_handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Facebook username affiliated with this podcast
    """

    google_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Google Podcasts url for this podcast
    """

    instagram_handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Instagram username affiliated with this podcast
    """

    linkedin_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    LinkedIn url affiliated with this podcast
    """

    patreon_handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Patreon username affiliated with this podcast
    """

    spotify_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Spotify url for this podcast
    """

    twitter_handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    Twitter username affiliated with this podcast
    """

    url1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url affiliated with this podcast
    """

    url2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url affiliated with this podcast
    """

    url3: typing.Optional[str] = pydantic.Field(default=None)
    """
    Url affiliated with this podcast
    """

    wechat_handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    WeChat username affiliated with this podcast
    """

    youtube_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    YouTube url affiliated with this podcast
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
