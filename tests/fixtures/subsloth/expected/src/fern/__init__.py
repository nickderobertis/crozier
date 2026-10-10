



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DateLike,
        DateTimeLike,
        DurationValue,
        Episode,
        EpisodeDetailResponse,
        ErrorResponse,
        ErrorResponseCode,
        ErrorResponseError,
        Id,
        ImageUrl,
        LanguageCode,
        Movie,
        MovieDetailResponse,
        MovieListResponse,
        MovieSummary,
        MovieTmdbId,
        PaginationMeta,
        Rating,
        ResolutionLabel,
        Show,
        ShowDetailResponse,
        ShowListResponse,
        ShowSummary,
        ShowSummaryPopularity,
        ShowSummaryTmdbId,
        ShowSummaryUserPopularity,
        ShowTmdbId,
        StringOrStringArray,
        SubtitleTrack,
        SubtitleTrackFormat,
        SubtitlesValue,
        SubtitlesValueOneValue,
        UnexpectedHtmlResponse,
        VideoQuality,
        VideoSource,
        VideoSourceType,
        Year,
    )
    from .errors import ForbiddenError, NotFoundError, PaymentRequiredError, ServiceUnavailableError, UnauthorizedError
    from . import episodes, movies, shows
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .movies import ListMoviesRequestSort
    from .shows import ListShowsRequestSort
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DateLike": ".types",
    "DateTimeLike": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DurationValue": ".types",
    "Episode": ".types",
    "EpisodeDetailResponse": ".types",
    "ErrorResponse": ".types",
    "ErrorResponseCode": ".types",
    "ErrorResponseError": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "Id": ".types",
    "ImageUrl": ".types",
    "LanguageCode": ".types",
    "ListMoviesRequestSort": ".movies",
    "ListShowsRequestSort": ".shows",
    "Movie": ".types",
    "MovieDetailResponse": ".types",
    "MovieListResponse": ".types",
    "MovieSummary": ".types",
    "MovieTmdbId": ".types",
    "NotFoundError": ".errors",
    "PaginationMeta": ".types",
    "PaymentRequiredError": ".errors",
    "Rating": ".types",
    "ResolutionLabel": ".types",
    "ServiceUnavailableError": ".errors",
    "Show": ".types",
    "ShowDetailResponse": ".types",
    "ShowListResponse": ".types",
    "ShowSummary": ".types",
    "ShowSummaryPopularity": ".types",
    "ShowSummaryTmdbId": ".types",
    "ShowSummaryUserPopularity": ".types",
    "ShowTmdbId": ".types",
    "StringOrStringArray": ".types",
    "SubtitleTrack": ".types",
    "SubtitleTrackFormat": ".types",
    "SubtitlesValue": ".types",
    "SubtitlesValueOneValue": ".types",
    "UnauthorizedError": ".errors",
    "UnexpectedHtmlResponse": ".types",
    "VideoQuality": ".types",
    "VideoSource": ".types",
    "VideoSourceType": ".types",
    "Year": ".types",
    "__version__": ".version",
    "episodes": ".episodes",
    "movies": ".movies",
    "shows": ".shows",
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
    "AsyncFernApi",
    "DateLike",
    "DateTimeLike",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DurationValue",
    "Episode",
    "EpisodeDetailResponse",
    "ErrorResponse",
    "ErrorResponseCode",
    "ErrorResponseError",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "Id",
    "ImageUrl",
    "LanguageCode",
    "ListMoviesRequestSort",
    "ListShowsRequestSort",
    "Movie",
    "MovieDetailResponse",
    "MovieListResponse",
    "MovieSummary",
    "MovieTmdbId",
    "NotFoundError",
    "PaginationMeta",
    "PaymentRequiredError",
    "Rating",
    "ResolutionLabel",
    "ServiceUnavailableError",
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
    "UnauthorizedError",
    "UnexpectedHtmlResponse",
    "VideoQuality",
    "VideoSource",
    "VideoSourceType",
    "Year",
    "__version__",
    "episodes",
    "movies",
    "shows",
]
