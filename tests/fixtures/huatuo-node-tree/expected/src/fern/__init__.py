



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ContainerMetadata,
        ContainerResponse,
        Error,
        ErrorCode,
        ErrorResponse,
        ObservationScope,
        Operation,
        OperationKind,
        OperationOutcome,
        OperationResponse,
        OperationStatus,
        OperationTerminal,
        ProfilingLanguage,
        ProfilingMode,
        ProfilingOperationSpec,
        ProfilingType,
        TracingOperationSpec,
        TracingType,
        WatchEvent,
        WatchEventData,
        WatchEventFilters,
        WatchEventSpecVersion,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ContentTooLargeError,
        InternalServerError,
        NotFoundError,
        NotImplementedError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
        UnprocessableEntityError,
        UnsupportedMediaTypeError,
    )
    from . import config, containers, events, operations, readiness
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .operations import StartOperationRequestSpec
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "ContainerMetadata": ".types",
    "ContainerResponse": ".types",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "ErrorCode": ".types",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "InternalServerError": ".errors",
    "NotFoundError": ".errors",
    "NotImplementedError": ".errors",
    "ObservationScope": ".types",
    "Operation": ".types",
    "OperationKind": ".types",
    "OperationOutcome": ".types",
    "OperationResponse": ".types",
    "OperationStatus": ".types",
    "OperationTerminal": ".types",
    "ProfilingLanguage": ".types",
    "ProfilingMode": ".types",
    "ProfilingOperationSpec": ".types",
    "ProfilingType": ".types",
    "ServiceUnavailableError": ".errors",
    "StartOperationRequestSpec": ".operations",
    "TooManyRequestsError": ".errors",
    "TracingOperationSpec": ".types",
    "TracingType": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "UnsupportedMediaTypeError": ".errors",
    "WatchEvent": ".types",
    "WatchEventData": ".types",
    "WatchEventFilters": ".types",
    "WatchEventSpecVersion": ".types",
    "__version__": ".version",
    "config": ".config",
    "containers": ".containers",
    "events": ".events",
    "operations": ".operations",
    "readiness": ".readiness",
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
    "ContainerMetadata",
    "ContainerResponse",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "ErrorCode",
    "ErrorResponse",
    "FernApi",
    "InternalServerError",
    "NotFoundError",
    "NotImplementedError",
    "ObservationScope",
    "Operation",
    "OperationKind",
    "OperationOutcome",
    "OperationResponse",
    "OperationStatus",
    "OperationTerminal",
    "ProfilingLanguage",
    "ProfilingMode",
    "ProfilingOperationSpec",
    "ProfilingType",
    "ServiceUnavailableError",
    "StartOperationRequestSpec",
    "TooManyRequestsError",
    "TracingOperationSpec",
    "TracingType",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "UnsupportedMediaTypeError",
    "WatchEvent",
    "WatchEventData",
    "WatchEventFilters",
    "WatchEventSpecVersion",
    "__version__",
    "config",
    "containers",
    "events",
    "operations",
    "readiness",
]
