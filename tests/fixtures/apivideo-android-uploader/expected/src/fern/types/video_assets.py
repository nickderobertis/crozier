

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VideoAssets(UniversalBaseModel):
    """
    Collection of details about the video object that you can use to work with the video object.
    """

    hls: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the manifest URL. For HTTP Live Streaming (HLS), when a HLS video stream is initiated, the first file to download is the manifest. This file has the extension M3U8, and provides the video player with information about the various bitrates available for streaming.
    """

    iframe: typing.Optional[str] = pydantic.Field(default=None)
    """
    Code to use video from a third party website
    """

    player: typing.Optional[str] = pydantic.Field(default=None)
    """
    Raw url of the player.
    """

    thumbnail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Poster of the video.
    """

    mp4: typing.Optional[str] = pydantic.Field(default=None)
    """
    Available only if mp4Support is enabled. Raw mp4 url.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
