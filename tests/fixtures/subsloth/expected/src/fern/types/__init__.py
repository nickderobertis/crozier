



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .date_like import DateLike
    from .date_time_like import DateTimeLike
    from .duration_value import DurationValue
    from .episode import Episode
    from .episode_detail_response import EpisodeDetailResponse
    from .error_response import ErrorResponse
    from .error_response_code import ErrorResponseCode
    from .error_response_error import ErrorResponseError
    from .id import Id
    from .image_url import ImageUrl
    from .language_code import LanguageCode
    from .movie import Movie
    from .movie_detail_response import MovieDetailResponse
    from .movie_list_response import MovieListResponse
    from .movie_summary import MovieSummary
    from .movie_tmdb_id import MovieTmdbId
    from .pagination_meta import PaginationMeta
    from .rating import Rating
    from .resolution_label import ResolutionLabel
    from .show import Show
    from .show_detail_response import ShowDetailResponse
    from .show_list_response import ShowListResponse
    from .show_summary import ShowSummary
    from .show_summary_popularity import ShowSummaryPopularity
    from .show_summary_tmdb_id import ShowSummaryTmdbId
    from .show_summary_user_popularity import ShowSummaryUserPopularity
    from .show_tmdb_id import ShowTmdbId
    from .string_or_string_array import StringOrStringArray
    from .subtitle_track import SubtitleTrack
    from .subtitle_track_format import SubtitleTrackFormat
    from .subtitles_value import SubtitlesValue
    from .subtitles_value_one_value import SubtitlesValueOneValue
    from .unexpected_html_response import UnexpectedHtmlResponse
    from .video_quality import VideoQuality
    from .video_source import VideoSource
    from .video_source_type import VideoSourceType
    from .year import Year
_dynamic_imports: typing.Dict[str, str] = {
    "DateLike": ".date_like",
    "DateTimeLike": ".date_time_like",
    "DurationValue": ".duration_value",
    "Episode": ".episode",
    "EpisodeDetailResponse": ".episode_detail_response",
    "ErrorResponse": ".error_response",
    "ErrorResponseCode": ".error_response_code",
    "ErrorResponseError": ".error_response_error",
    "Id": ".id",
    "ImageUrl": ".image_url",
    "LanguageCode": ".language_code",
    "Movie": ".movie",
    "MovieDetailResponse": ".movie_detail_response",
    "MovieListResponse": ".movie_list_response",
    "MovieSummary": ".movie_summary",
    "MovieTmdbId": ".movie_tmdb_id",
    "PaginationMeta": ".pagination_meta",
    "Rating": ".rating",
    "ResolutionLabel": ".resolution_label",
    "Show": ".show",
    "ShowDetailResponse": ".show_detail_response",
    "ShowListResponse": ".show_list_response",
    "ShowSummary": ".show_summary",
    "ShowSummaryPopularity": ".show_summary_popularity",
    "ShowSummaryTmdbId": ".show_summary_tmdb_id",
    "ShowSummaryUserPopularity": ".show_summary_user_popularity",
    "ShowTmdbId": ".show_tmdb_id",
    "StringOrStringArray": ".string_or_string_array",
    "SubtitleTrack": ".subtitle_track",
    "SubtitleTrackFormat": ".subtitle_track_format",
    "SubtitlesValue": ".subtitles_value",
    "SubtitlesValueOneValue": ".subtitles_value_one_value",
    "UnexpectedHtmlResponse": ".unexpected_html_response",
    "VideoQuality": ".video_quality",
    "VideoSource": ".video_source",
    "VideoSourceType": ".video_source_type",
    "Year": ".year",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "DateLike",
    "DateTimeLike",
    "DurationValue",
    "Episode",
    "EpisodeDetailResponse",
    "ErrorResponse",
    "ErrorResponseCode",
    "ErrorResponseError",
    "Id",
    "ImageUrl",
    "LanguageCode",
    "Movie",
    "MovieDetailResponse",
    "MovieListResponse",
    "MovieSummary",
    "MovieTmdbId",
    "PaginationMeta",
    "Rating",
    "ResolutionLabel",
    "Show",
    "ShowDetailResponse",
    "ShowListResponse",
    "ShowSummary",
    "ShowSummaryPopularity",
    "ShowSummaryTmdbId",
    "ShowSummaryUserPopularity",
    "ShowTmdbId",
    "StringOrStringArray",
    "SubtitleTrack",
    "SubtitleTrackFormat",
    "SubtitlesValue",
    "SubtitlesValueOneValue",
    "UnexpectedHtmlResponse",
    "VideoQuality",
    "VideoSource",
    "VideoSourceType",
    "Year",
]
