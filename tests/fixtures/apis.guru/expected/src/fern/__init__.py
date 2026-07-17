



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import ApIs, Api, ApiVersion, Metrics, MetricsThisWeek
    from . import ap_is
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .ap_is import GetProvidersResponse, GetServicesResponse
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ApIs": ".types",
    "Api": ".types",
    "ApiVersion": ".types",
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetProvidersResponse": ".ap_is",
    "GetServicesResponse": ".ap_is",
    "Metrics": ".types",
    "MetricsThisWeek": ".types",
    "__version__": ".version",
    "ap_is": ".ap_is",
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
    "ApIs",
    "Api",
    "ApiVersion",
    "AsyncFernApi",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetProvidersResponse",
    "GetServicesResponse",
    "Metrics",
    "MetricsThisWeek",
    "__version__",
    "ap_is",
]
