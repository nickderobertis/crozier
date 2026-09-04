



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_token import AccessToken
    from .additional_bad_request_errors import AdditionalBadRequestErrors
    from .bad_request import BadRequest
    from .metadata import Metadata
    from .not_found import NotFound
    from .too_many_requests import TooManyRequests
    from .video import Video
    from .video_assets import VideoAssets
    from .video_language_origin import VideoLanguageOrigin
    from .video_source import VideoSource
    from .video_source_live_stream import VideoSourceLiveStream
    from .video_source_live_stream_link import VideoSourceLiveStreamLink
_dynamic_imports: typing.Dict[str, str] = {
    "AccessToken": ".access_token",
    "AdditionalBadRequestErrors": ".additional_bad_request_errors",
    "BadRequest": ".bad_request",
    "Metadata": ".metadata",
    "NotFound": ".not_found",
    "TooManyRequests": ".too_many_requests",
    "Video": ".video",
    "VideoAssets": ".video_assets",
    "VideoLanguageOrigin": ".video_language_origin",
    "VideoSource": ".video_source",
    "VideoSourceLiveStream": ".video_source_live_stream",
    "VideoSourceLiveStreamLink": ".video_source_live_stream_link",
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
    "AccessToken",
    "AdditionalBadRequestErrors",
    "BadRequest",
    "Metadata",
    "NotFound",
    "TooManyRequests",
    "Video",
    "VideoAssets",
    "VideoLanguageOrigin",
    "VideoSource",
    "VideoSourceLiveStream",
    "VideoSourceLiveStreamLink",
]
