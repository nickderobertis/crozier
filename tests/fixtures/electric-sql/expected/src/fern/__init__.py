



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ConflictErrorBodyItem,
        ConflictErrorBodyItemHeaders,
        ConflictErrorBodyItemHeadersControl,
        GetV1ShapeRequestLog,
        GetV1ShapeRequestReplica,
        GetV1ShapeResponse,
        GetV1ShapeResponseData,
        GetV1ShapeResponseDataDataItem,
        GetV1ShapeResponseDataDataItemHeaders,
        GetV1ShapeResponseDataDataItemHeadersOperation,
        GetV1ShapeResponseDataMetadata,
        GetV1ShapeResponseZeroItem,
        GetV1ShapeResponseZeroItemHeaders,
        GetV1ShapeResponseZeroItemHeadersControl,
        GetV1ShapeResponseZeroItemHeadersOperation,
        PostV1ShapeRequestLog,
        PostV1ShapeRequestReplica,
        PostV1ShapeResponse,
        PostV1ShapeResponseDataItem,
        PostV1ShapeResponseMetadata,
        TooManyRequestsErrorBody,
    )
    from .errors import BadRequestError, ConflictError, ContentTooLargeError, NotFoundError, TooManyRequestsError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "ConflictErrorBodyItem": ".types",
    "ConflictErrorBodyItemHeaders": ".types",
    "ConflictErrorBodyItemHeadersControl": ".types",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetV1ShapeRequestLog": ".types",
    "GetV1ShapeRequestReplica": ".types",
    "GetV1ShapeResponse": ".types",
    "GetV1ShapeResponseData": ".types",
    "GetV1ShapeResponseDataDataItem": ".types",
    "GetV1ShapeResponseDataDataItemHeaders": ".types",
    "GetV1ShapeResponseDataDataItemHeadersOperation": ".types",
    "GetV1ShapeResponseDataMetadata": ".types",
    "GetV1ShapeResponseZeroItem": ".types",
    "GetV1ShapeResponseZeroItemHeaders": ".types",
    "GetV1ShapeResponseZeroItemHeadersControl": ".types",
    "GetV1ShapeResponseZeroItemHeadersOperation": ".types",
    "NotFoundError": ".errors",
    "PostV1ShapeRequestLog": ".types",
    "PostV1ShapeRequestReplica": ".types",
    "PostV1ShapeResponse": ".types",
    "PostV1ShapeResponseDataItem": ".types",
    "PostV1ShapeResponseMetadata": ".types",
    "TooManyRequestsError": ".errors",
    "TooManyRequestsErrorBody": ".types",
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
    "ConflictError",
    "ConflictErrorBodyItem",
    "ConflictErrorBodyItemHeaders",
    "ConflictErrorBodyItemHeadersControl",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetV1ShapeRequestLog",
    "GetV1ShapeRequestReplica",
    "GetV1ShapeResponse",
    "GetV1ShapeResponseData",
    "GetV1ShapeResponseDataDataItem",
    "GetV1ShapeResponseDataDataItemHeaders",
    "GetV1ShapeResponseDataDataItemHeadersOperation",
    "GetV1ShapeResponseDataMetadata",
    "GetV1ShapeResponseZeroItem",
    "GetV1ShapeResponseZeroItemHeaders",
    "GetV1ShapeResponseZeroItemHeadersControl",
    "GetV1ShapeResponseZeroItemHeadersOperation",
    "NotFoundError",
    "PostV1ShapeRequestLog",
    "PostV1ShapeRequestReplica",
    "PostV1ShapeResponse",
    "PostV1ShapeResponseDataItem",
    "PostV1ShapeResponseMetadata",
    "TooManyRequestsError",
    "TooManyRequestsErrorBody",
    "__version__",
]
