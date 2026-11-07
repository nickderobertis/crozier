



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import Agents, AgentsAgentsItem, AriForm, AriFormCborHex, AriFormUri, TextEid, Version
    from .errors import (
        BadRequestError,
        GatewayTimeoutError,
        NotFoundError,
        UnprocessableEntityError,
        UnsupportedMediaTypeError,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Agents": ".types",
    "AgentsAgentsItem": ".types",
    "AriForm": ".types",
    "AriFormCborHex": ".types",
    "AriFormUri": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GatewayTimeoutError": ".errors",
    "NotFoundError": ".errors",
    "TextEid": ".types",
    "UnprocessableEntityError": ".errors",
    "UnsupportedMediaTypeError": ".errors",
    "Version": ".types",
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
    "Agents",
    "AgentsAgentsItem",
    "AriForm",
    "AriFormCborHex",
    "AriFormUri",
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GatewayTimeoutError",
    "NotFoundError",
    "TextEid",
    "UnprocessableEntityError",
    "UnsupportedMediaTypeError",
    "Version",
    "__version__",
]
