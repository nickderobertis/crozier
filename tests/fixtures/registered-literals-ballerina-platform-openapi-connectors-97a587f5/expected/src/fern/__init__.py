



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Capabilities,
        Deprecation,
        Error,
        ErrorCode,
        ErrorResponse,
        Event,
        EventList,
        File,
        FileList,
        FileStatistics,
        FineTune,
        FineTuneList,
        HyperParameters,
        InnerError,
        InnerErrorCode,
        LifeCycleStatus,
        LogLevel,
        Model,
        ModelList,
        Purpose,
        ScaleType,
        State,
        TypeDiscriminator,
    )
    from . import files, fine_tunes, models
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .files import FilesUploadRequestPurpose
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "Capabilities": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Deprecation": ".types",
    "Error": ".types",
    "ErrorCode": ".types",
    "ErrorResponse": ".types",
    "Event": ".types",
    "EventList": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "File": ".types",
    "FileList": ".types",
    "FileStatistics": ".types",
    "FilesUploadRequestPurpose": ".files",
    "FineTune": ".types",
    "FineTuneList": ".types",
    "HyperParameters": ".types",
    "InnerError": ".types",
    "InnerErrorCode": ".types",
    "LifeCycleStatus": ".types",
    "LogLevel": ".types",
    "Model": ".types",
    "ModelList": ".types",
    "Purpose": ".types",
    "ScaleType": ".types",
    "State": ".types",
    "TypeDiscriminator": ".types",
    "__version__": ".version",
    "files": ".files",
    "fine_tunes": ".fine_tunes",
    "models": ".models",
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
    "Capabilities",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Deprecation",
    "Error",
    "ErrorCode",
    "ErrorResponse",
    "Event",
    "EventList",
    "FernApi",
    "FernApiEnvironment",
    "File",
    "FileList",
    "FileStatistics",
    "FilesUploadRequestPurpose",
    "FineTune",
    "FineTuneList",
    "HyperParameters",
    "InnerError",
    "InnerErrorCode",
    "LifeCycleStatus",
    "LogLevel",
    "Model",
    "ModelList",
    "Purpose",
    "ScaleType",
    "State",
    "TypeDiscriminator",
    "__version__",
    "files",
    "fine_tunes",
    "models",
]
