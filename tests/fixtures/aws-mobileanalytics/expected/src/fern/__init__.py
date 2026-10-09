



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestException,
        Double,
        Event,
        EventListDefinition,
        EventSession,
        Iso8601Timestamp,
        Long,
        MapOfStringToNumber,
        MapOfStringToString,
        PutEventsInput,
        Session,
        String,
        String0To1000Chars,
        String10Chars,
        String50Chars,
    )
    from .errors import BadRequestError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestException": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Double": ".types",
    "Event": ".types",
    "EventListDefinition": ".types",
    "EventSession": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Iso8601Timestamp": ".types",
    "Long": ".types",
    "MapOfStringToNumber": ".types",
    "MapOfStringToString": ".types",
    "PutEventsInput": ".types",
    "Session": ".types",
    "String": ".types",
    "String0To1000Chars": ".types",
    "String10Chars": ".types",
    "String50Chars": ".types",
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
    "BadRequestError",
    "BadRequestException",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Double",
    "Event",
    "EventListDefinition",
    "EventSession",
    "FernApi",
    "FernApiEnvironment",
    "Iso8601Timestamp",
    "Long",
    "MapOfStringToNumber",
    "MapOfStringToString",
    "PutEventsInput",
    "Session",
    "String",
    "String0To1000Chars",
    "String10Chars",
    "String50Chars",
    "__version__",
]
