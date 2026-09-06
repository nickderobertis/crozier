



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Audio,
        Error,
        Image,
        PaginatedAudioResults,
        PaginatedImageResults,
        ReportRequest,
        ReportRequestReason,
        SourceStats,
        Tag,
    )
    from .errors import BadRequestError, NotFoundError, TooManyRequestsError, UnauthorizedError
    from . import audio, auth, images
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .audio import GetAudioWaveformResponse, SearchAudioRequestCategory, SearchAudioRequestLength
    from .auth import (
        GetAccessTokenRequestGrantType,
        GetAccessTokenResponse,
        GetRateLimitResponse,
        RegisterApplicationResponse,
    )
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .images import (
        GetImageOembedResponse,
        SearchImagesRequestAspectRatio,
        SearchImagesRequestCategory,
        SearchImagesRequestSize,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Audio": ".types",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetAccessTokenRequestGrantType": ".auth",
    "GetAccessTokenResponse": ".auth",
    "GetAudioWaveformResponse": ".audio",
    "GetImageOembedResponse": ".images",
    "GetRateLimitResponse": ".auth",
    "Image": ".types",
    "NotFoundError": ".errors",
    "PaginatedAudioResults": ".types",
    "PaginatedImageResults": ".types",
    "RegisterApplicationResponse": ".auth",
    "ReportRequest": ".types",
    "ReportRequestReason": ".types",
    "SearchAudioRequestCategory": ".audio",
    "SearchAudioRequestLength": ".audio",
    "SearchImagesRequestAspectRatio": ".images",
    "SearchImagesRequestCategory": ".images",
    "SearchImagesRequestSize": ".images",
    "SourceStats": ".types",
    "Tag": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "audio": ".audio",
    "auth": ".auth",
    "images": ".images",
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
    "Audio",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "GetAccessTokenRequestGrantType",
    "GetAccessTokenResponse",
    "GetAudioWaveformResponse",
    "GetImageOembedResponse",
    "GetRateLimitResponse",
    "Image",
    "NotFoundError",
    "PaginatedAudioResults",
    "PaginatedImageResults",
    "RegisterApplicationResponse",
    "ReportRequest",
    "ReportRequestReason",
    "SearchAudioRequestCategory",
    "SearchAudioRequestLength",
    "SearchImagesRequestAspectRatio",
    "SearchImagesRequestCategory",
    "SearchImagesRequestSize",
    "SourceStats",
    "Tag",
    "TooManyRequestsError",
    "UnauthorizedError",
    "__version__",
    "audio",
    "auth",
    "images",
]
