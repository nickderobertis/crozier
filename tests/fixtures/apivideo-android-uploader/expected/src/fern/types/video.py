

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .metadata import Metadata
from .video_assets import VideoAssets
from .video_language_origin import VideoLanguageOrigin
from .video_source import VideoSource


class Video(UniversalBaseModel):
    video_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="videoId"),
        pydantic.Field(alias="videoId", description="The unique identifier of the video object."),
    ]
    """
    The unique identifier of the video object.
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When a video was created, presented in ATOM UTC format."),
    ] = None
    """
    When a video was created, presented in ATOM UTC format.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The title of the video content.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    A description for the video content.
    """

    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="publishedAt"),
        pydantic.Field(
            alias="publishedAt",
            description="The date and time the API created the video. Date and time are provided using ATOM UTC format.",
        ),
    ] = None
    """
    The date and time the API created the video. Date and time are provided using ATOM UTC format.
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(
            alias="updatedAt",
            description="The date and time the video was updated. Date and time are provided using ATOM UTC format.",
        ),
    ] = None
    """
    The date and time the video was updated. Date and time are provided using ATOM UTC format.
    """

    discarded_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="discardedAt"),
        pydantic.Field(
            alias="discardedAt",
            description="The date and time the video was discarded. The API populates this field only if you have the Video Restore feature enabled and discard a video. Date and time are provided using ATOM UTC format.",
        ),
    ] = None
    """
    The date and time the video was discarded. The API populates this field only if you have the Video Restore feature enabled and discard a video. Date and time are provided using ATOM UTC format.
    """

    deletes_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletesAt"),
        pydantic.Field(
            alias="deletesAt",
            description="The date and time the video will be permanently deleted. The API populates this field only if you have the Video Restore feature enabled and discard a video. Discarded videos are pemanently deleted after 90 days. Date and time are provided using ATOM UTC format.",
        ),
    ] = None
    """
    The date and time the video will be permanently deleted. The API populates this field only if you have the Video Restore feature enabled and discard a video. Discarded videos are pemanently deleted after 90 days. Date and time are provided using ATOM UTC format.
    """

    discarded: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Returns `true` for videos you discarded when you have the Video Restore feature enabled. Returns `false` for every other video.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Returns the language of a video in [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag) format. You can set the language during video creation via the API, otherwise it is detected automatically.
    """

    language_origin: typing_extensions.Annotated[
        typing.Optional[VideoLanguageOrigin],
        FieldMetadata(alias="languageOrigin"),
        pydantic.Field(
            alias="languageOrigin",
            description="Returns the origin of the last update on the video's `language` attribute.\n\n- `api` means that the last update was requested from the API.\n- `auto` means that the last update was done automatically by the API.",
        ),
    ] = None
    """
    Returns the origin of the last update on the video's `language` attribute.
    
    - `api` means that the last update was requested from the API.
    - `auto` means that the last update was done automatically by the API.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    One array of tags (each tag is a string) in order to categorize a video. Tags may include spaces. 
    """

    metadata: typing.Optional[typing.List[Metadata]] = pydantic.Field(default=None)
    """
    Metadata you can use to categorise and filter videos. Metadata is a list of dictionaries, where each dictionary represents a key value pair for categorising a video.
    """

    source: typing.Optional[VideoSource] = None
    assets: typing.Optional[VideoAssets] = None
    player_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="playerId"),
        pydantic.Field(alias="playerId", description="The id of the player that will be applied on the video."),
    ] = None
    """
    The id of the player that will be applied on the video.
    """

    public: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Defines if the content is publicly reachable or if a unique token is needed for each play session. Default is true. Tutorials on [private videos](https://api.video/blog/endpoints/private-videos/).
    """

    panoramic: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Defines if video is panoramic.
    """

    mp4support: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="mp4Support"),
        pydantic.Field(
            alias="mp4Support",
            description="This lets you know whether mp4 is supported. If enabled, an mp4 URL will be provided in the response for the video.",
        ),
    ] = None
    """
    This lets you know whether mp4 is supported. If enabled, an mp4 URL will be provided in the response for the video.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
