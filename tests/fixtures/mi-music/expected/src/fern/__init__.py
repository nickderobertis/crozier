



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CmdStatusResp,
        DownloadJsonResp,
        HttpValidationError,
        LatestVersionResp,
        MusicInfoItem,
        MusicInfoResp,
        PlayListMusicObj,
        PlayListObj,
        PlayingMusicResp,
        PlaylistMusicsResp,
        PlaylistNamesResp,
        RetMsg,
        SetVolumeResp,
        UploadCookieResp,
        ValidationError,
        ValidationErrorLocItem,
        VersionResp,
        VolumeResp,
        WsTokenResp,
    )
    from .errors import BadGatewayError, BadRequestError, GatewayTimeoutError, NotFoundError, UnprocessableEntityError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadGatewayError": ".errors",
    "BadRequestError": ".errors",
    "CmdStatusResp": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DownloadJsonResp": ".types",
    "FernApi": ".client",
    "GatewayTimeoutError": ".errors",
    "HttpValidationError": ".types",
    "LatestVersionResp": ".types",
    "MusicInfoItem": ".types",
    "MusicInfoResp": ".types",
    "NotFoundError": ".errors",
    "PlayListMusicObj": ".types",
    "PlayListObj": ".types",
    "PlayingMusicResp": ".types",
    "PlaylistMusicsResp": ".types",
    "PlaylistNamesResp": ".types",
    "RetMsg": ".types",
    "SetVolumeResp": ".types",
    "UnprocessableEntityError": ".errors",
    "UploadCookieResp": ".types",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "VersionResp": ".types",
    "VolumeResp": ".types",
    "WsTokenResp": ".types",
    "__version__": ".version",
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
    "BadGatewayError",
    "BadRequestError",
    "CmdStatusResp",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DownloadJsonResp",
    "FernApi",
    "GatewayTimeoutError",
    "HttpValidationError",
    "LatestVersionResp",
    "MusicInfoItem",
    "MusicInfoResp",
    "NotFoundError",
    "PlayListMusicObj",
    "PlayListObj",
    "PlayingMusicResp",
    "PlaylistMusicsResp",
    "PlaylistNamesResp",
    "RetMsg",
    "SetVolumeResp",
    "UnprocessableEntityError",
    "UploadCookieResp",
    "ValidationError",
    "ValidationErrorLocItem",
    "VersionResp",
    "VolumeResp",
    "WsTokenResp",
    "__version__",
]
