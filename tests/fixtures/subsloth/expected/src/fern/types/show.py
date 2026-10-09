

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .duration_value import DurationValue
from .episode import Episode
from .id import Id
from .image_url import ImageUrl
from .rating import Rating
from .show_summary_popularity import ShowSummaryPopularity
from .show_summary_user_popularity import ShowSummaryUserPopularity
from .show_tmdb_id import ShowTmdbId
from .string_or_string_array import StringOrStringArray
from .year import Year


class Show(UniversalBaseModel):
    """
    Full show detail with seasons and episodes.
    """

    imdb_id: typing.Optional[str] = None
    tmdb_id: typing.Optional[ShowTmdbId] = None
    seasons: typing.Optional[int] = pydantic.Field(default=None)
    """
    Season count as integer, as observed in live Kodi API responses (e.g. 1).
    """

    episodes: typing.Optional[typing.List[Episode]] = None
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
    fanart: typing.Optional[ImageUrl] = None
    rating: typing.Optional[Rating] = None
    imdb_rating: typing.Optional[Rating] = None
    year: typing.Optional[Year] = None
    release_year: typing.Optional[Year] = None
    genres: typing.Optional[StringOrStringArray] = None
    array_genres: typing.Optional[typing.List[str]] = None
    countries: typing.Optional[StringOrStringArray] = None
    array_countries: typing.Optional[typing.List[str]] = None
    status: typing.Optional[str] = None
    ended: typing.Optional[bool] = None
    duration: typing.Optional[DurationValue] = None
    length: typing.Optional[DurationValue] = None
    newest_video: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp (seconds) of the most recently published episode, as observed in live Kodi API responses.
    """

    popularity: typing.Optional[ShowSummaryPopularity] = None
    user_popularity: typing.Optional[ShowSummaryUserPopularity] = None
    desc: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
