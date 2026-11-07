



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        BadRequestErrorBodyExtra,
        DeleteRequestEvent,
        DeleteRequestStart,
        DownloadRequestEvent,
        DownloadRequestStart,
        EventType,
        HeadDownloadRequestEvent,
        HeadDownloadRequestStart,
        ListOrder,
        ListRequestAfter,
        ListRequestBefore,
        ListRequestEvent,
        ListRequestLimit,
        ListRequestOffset,
        ListRequestOrder,
        ListResponseResults,
        NaiveDatetime,
        NotFoundErrorBody,
        NotFoundErrorBodyExtra,
        Parameters,
        Recording,
        SubscribeRequestTypes,
        TestRequestParameters,
        TestResponseResult,
        UploadRequestEvent,
        UploadRequestStart,
        UploadRequestType,
    )
    from .errors import BadRequestError, NotFoundError
    from . import ping, recordings, sse, test
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .recordings import (
        RecordingsEventListRequestAfter,
        RecordingsEventListRequestBefore,
        RecordingsEventListRequestLimit,
        RecordingsEventListRequestOffset,
        RecordingsEventListRequestOrder,
    )
    from .sse import SseSubscribeRequestTypes
    from .test import TestTestRequestParameters
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "BadRequestErrorBodyExtra": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeleteRequestEvent": ".types",
    "DeleteRequestStart": ".types",
    "DownloadRequestEvent": ".types",
    "DownloadRequestStart": ".types",
    "EventType": ".types",
    "FernApi": ".client",
    "HeadDownloadRequestEvent": ".types",
    "HeadDownloadRequestStart": ".types",
    "ListOrder": ".types",
    "ListRequestAfter": ".types",
    "ListRequestBefore": ".types",
    "ListRequestEvent": ".types",
    "ListRequestLimit": ".types",
    "ListRequestOffset": ".types",
    "ListRequestOrder": ".types",
    "ListResponseResults": ".types",
    "NaiveDatetime": ".types",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "NotFoundErrorBodyExtra": ".types",
    "Parameters": ".types",
    "Recording": ".types",
    "RecordingsEventListRequestAfter": ".recordings",
    "RecordingsEventListRequestBefore": ".recordings",
    "RecordingsEventListRequestLimit": ".recordings",
    "RecordingsEventListRequestOffset": ".recordings",
    "RecordingsEventListRequestOrder": ".recordings",
    "SseSubscribeRequestTypes": ".sse",
    "SubscribeRequestTypes": ".types",
    "TestRequestParameters": ".types",
    "TestResponseResult": ".types",
    "TestTestRequestParameters": ".test",
    "UploadRequestEvent": ".types",
    "UploadRequestStart": ".types",
    "UploadRequestType": ".types",
    "__version__": ".version",
    "ping": ".ping",
    "recordings": ".recordings",
    "sse": ".sse",
    "test": ".test",
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
    "BadRequestErrorBody",
    "BadRequestErrorBodyExtra",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeleteRequestEvent",
    "DeleteRequestStart",
    "DownloadRequestEvent",
    "DownloadRequestStart",
    "EventType",
    "FernApi",
    "HeadDownloadRequestEvent",
    "HeadDownloadRequestStart",
    "ListOrder",
    "ListRequestAfter",
    "ListRequestBefore",
    "ListRequestEvent",
    "ListRequestLimit",
    "ListRequestOffset",
    "ListRequestOrder",
    "ListResponseResults",
    "NaiveDatetime",
    "NotFoundError",
    "NotFoundErrorBody",
    "NotFoundErrorBodyExtra",
    "Parameters",
    "Recording",
    "RecordingsEventListRequestAfter",
    "RecordingsEventListRequestBefore",
    "RecordingsEventListRequestLimit",
    "RecordingsEventListRequestOffset",
    "RecordingsEventListRequestOrder",
    "SseSubscribeRequestTypes",
    "SubscribeRequestTypes",
    "TestRequestParameters",
    "TestResponseResult",
    "TestTestRequestParameters",
    "UploadRequestEvent",
    "UploadRequestStart",
    "UploadRequestType",
    "__version__",
    "ping",
    "recordings",
    "sse",
    "test",
]
