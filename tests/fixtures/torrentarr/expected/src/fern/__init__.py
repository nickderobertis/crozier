



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ConfigUpdateResponse,
        ConfigUpdateResponseReloadType,
        LogSearchMatch,
        LogSearchResponse,
        LogTailPayload,
        UnauthorizedErrorBody,
    )
    from .errors import (
        BadRequestError,
        ForbiddenError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import auth, system, web_ui
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .system import HealthResponse
    from .version import __version__
    from .web_ui import (
        ApiArrOpenItemRequestKind,
        ApiLogContentRequestFormat,
        ApiLogSearchRequestCase,
        ApiLogSearchRequestIncludeRotated,
        ApiLogSearchRequestRegex,
        WebArrOpenItemRequestKind,
        WebLogContentRequestFormat,
        WebLogSearchRequestCase,
        WebLogSearchRequestIncludeRotated,
        WebLogSearchRequestRegex,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ApiArrOpenItemRequestKind": ".web_ui",
    "ApiLogContentRequestFormat": ".web_ui",
    "ApiLogSearchRequestCase": ".web_ui",
    "ApiLogSearchRequestIncludeRotated": ".web_ui",
    "ApiLogSearchRequestRegex": ".web_ui",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConfigUpdateResponse": ".types",
    "ConfigUpdateResponseReloadType": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "HealthResponse": ".system",
    "LogSearchMatch": ".types",
    "LogSearchResponse": ".types",
    "LogTailPayload": ".types",
    "NotFoundError": ".errors",
    "ServiceUnavailableError": ".errors",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "WebArrOpenItemRequestKind": ".web_ui",
    "WebLogContentRequestFormat": ".web_ui",
    "WebLogSearchRequestCase": ".web_ui",
    "WebLogSearchRequestIncludeRotated": ".web_ui",
    "WebLogSearchRequestRegex": ".web_ui",
    "__version__": ".version",
    "auth": ".auth",
    "system": ".system",
    "web_ui": ".web_ui",
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
    "ApiArrOpenItemRequestKind",
    "ApiLogContentRequestFormat",
    "ApiLogSearchRequestCase",
    "ApiLogSearchRequestIncludeRotated",
    "ApiLogSearchRequestRegex",
    "AsyncFernApi",
    "BadRequestError",
    "ConfigUpdateResponse",
    "ConfigUpdateResponseReloadType",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "HealthResponse",
    "LogSearchMatch",
    "LogSearchResponse",
    "LogTailPayload",
    "NotFoundError",
    "ServiceUnavailableError",
    "TooManyRequestsError",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "WebArrOpenItemRequestKind",
    "WebLogContentRequestFormat",
    "WebLogSearchRequestCase",
    "WebLogSearchRequestIncludeRotated",
    "WebLogSearchRequestRegex",
    "__version__",
    "auth",
    "system",
    "web_ui",
]
