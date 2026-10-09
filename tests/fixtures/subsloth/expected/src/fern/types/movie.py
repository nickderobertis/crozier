

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .date_time_like import DateTimeLike
from .duration_value import DurationValue
from .id import Id
from .image_url import ImageUrl
from .movie_tmdb_id import MovieTmdbId
from .rating import Rating
from .resolution_label import ResolutionLabel
from .string_or_string_array import StringOrStringArray
from .subtitles_value import SubtitlesValue
from .video_quality import VideoQuality
from .video_source import VideoSource
from .year import Year


class Movie(UniversalBaseModel):
    """
    Full movie detail including streams, qualities, and playback URLs.
    """

    imdb_id: typing.Optional[str] = None
    tmdb_id: typing.Optional[MovieTmdbId] = None
    trailer: typing.Optional[str] = None
    trailer_url: typing.Optional[str] = None
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Movie stream URL or playback URL. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    download_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Movie download URL when available. May be signed; never persist in fixtures, database, preferences, diagnostics, or logs.
    """

    qualities: typing.Optional[typing.List[VideoQuality]] = None
    videos: typing.Optional[typing.List[VideoSource]] = None
    id: Id
    slug: typing.Optional[str] = None
    name: typing.Optional[str] = None
    title: typing.Optional[str] = None
    plot: typing.Optional[str] = None
    description: typing.Optional[str] = None
    poster: typing.Optional[ImageUrl] = None
    poster_url: typing.Optional[ImageUrl] = None
    poster_thumb: typing.Optional[ImageUrl] = None
    backdrop: typing.Optional[ImageUrl] = None
    backdrop_url: typing.Optional[ImageUrl] = None
    rating: typing.Optional[Rating] = None
    imdb_rating: typing.Optional[Rating] = None
    year: typing.Optional[Year] = None
    release_year: typing.Optional[Year] = None
    genres: typing.Optional[StringOrStringArray] = None
    array_genres: typing.Optional[typing.List[str]] = None
    countries: typing.Optional[StringOrStringArray] = None
    duration: typing.Optional[DurationValue] = None
    resolution: typing.Optional[ResolutionLabel] = None
    subtitles: typing.Optional[SubtitlesValue] = None
    desc: typing.Optional[str] = None
    updated_at: typing.Optional[DateTimeLike] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
