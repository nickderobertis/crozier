



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AnnotatedSignature,
        BatchResponse,
        GenericProperty,
        Property,
        PropertyDecimals,
        PropertyDescription,
        PropertyLogo,
        PropertyName,
        PropertyTicker,
        PropertyUrl,
    )
    from .errors import BadRequestError, NotFoundError
    from . import query
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .query import PostMetadataQueryResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AnnotatedSignature": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BatchResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GenericProperty": ".types",
    "NotFoundError": ".errors",
    "PostMetadataQueryResponse": ".query",
    "Property": ".types",
    "PropertyDecimals": ".types",
    "PropertyDescription": ".types",
    "PropertyLogo": ".types",
    "PropertyName": ".types",
    "PropertyTicker": ".types",
    "PropertyUrl": ".types",
    "__version__": ".version",
    "query": ".query",
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
    "AnnotatedSignature",
    "AsyncFernApi",
    "BadRequestError",
    "BatchResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GenericProperty",
    "NotFoundError",
    "PostMetadataQueryResponse",
    "Property",
    "PropertyDecimals",
    "PropertyDescription",
    "PropertyLogo",
    "PropertyName",
    "PropertyTicker",
    "PropertyUrl",
    "__version__",
    "query",
]
