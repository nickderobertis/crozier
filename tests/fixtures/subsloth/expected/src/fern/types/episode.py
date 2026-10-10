

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_like import DateLike
from .date_time_like import DateTimeLike
from .duration_value import DurationValue
from .id import Id
from .resolution_label import ResolutionLabel
from .subtitles_value import SubtitlesValue
from .video_quality import VideoQuality


class Episode(UniversalBaseModel):
    """
    Episode playback detail with stream URLs, qualities, subtitles, and metadata.
    """

    id: Id
    video_id: typing.Optional[Id] = None
    show_id: typing.Optional[Id] = None
    season: typing.Optional[int] = None
    number: typing.Optional[int] = None
    episode: typing.Optional[int] = None
    title: typing.Optional[str] = None
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Episode title in show episode lists; movie name in movie detail responses.
    """

    show_name: typing.Optional[str] = None
    plot: typing.Optional[str] = None
    description: typing.Optional[str] = None
    airdate: typing.Optional[DateLike] = None
    air_date: typing.Optional[DateLike] = None
    premiere_date: typing.Optional[DateLike] = None
    available: typing.Optional[bool] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Episode stream URL or playback URL. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Episode download URL when available. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    resolution: typing.Optional[ResolutionLabel] = None
    qualities: typing.Optional[typing.List[VideoQuality]] = None
    subtitles: typing.Optional[SubtitlesValue] = None
    duration: typing.Optional[DurationValue] = None
    created_at: typing.Optional[DateTimeLike] = None
    updated_at: typing.Optional[DateTimeLike] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
