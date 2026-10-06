



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BridgeStatus,
        ClientSnapshot,
        DeleteRecordingResult,
        DownloadTicket,
        ErrorDetail,
        ErrorResponse,
        HttpValidationError,
        LevelSnapshot,
        RecordingCapabilities,
        RecordingFormat,
        RecordingFormatCodec,
        RecordingFormatContainer,
        RecordingLimits,
        RecordingList,
        RecordingResult,
        RecordingSnapshot,
        RecordingSnapshotSource,
        RecordingSnapshotSourceTwo,
        RecordingSnapshotState,
        RecordingStorage,
        SourceLifecycle,
        SourceLifecycleAdmission,
        SourceLifecycleState,
        SourceLifecycleTransport,
        SourceSnapshot,
        TransportKeyDeleteResult,
        TransportKeyResult,
        TransportModeRequestMode,
        TransportSnapshot,
        TransportSnapshotMode,
        UnlockResult,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ContentTooLargeError,
        InsufficientStorageError,
        NotFoundError,
        ServiceUnavailableError,
        UnauthorizedError,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BridgeStatus": ".types",
    "ClientSnapshot": ".types",
    "ConflictError": ".errors",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DeleteRecordingResult": ".types",
    "DownloadTicket": ".types",
    "ErrorDetail": ".types",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "HttpValidationError": ".types",
    "InsufficientStorageError": ".errors",
    "LevelSnapshot": ".types",
    "NotFoundError": ".errors",
    "RecordingCapabilities": ".types",
    "RecordingFormat": ".types",
    "RecordingFormatCodec": ".types",
    "RecordingFormatContainer": ".types",
    "RecordingLimits": ".types",
    "RecordingList": ".types",
    "RecordingResult": ".types",
    "RecordingSnapshot": ".types",
    "RecordingSnapshotSource": ".types",
    "RecordingSnapshotSourceTwo": ".types",
    "RecordingSnapshotState": ".types",
    "RecordingStorage": ".types",
    "ServiceUnavailableError": ".errors",
    "SourceLifecycle": ".types",
    "SourceLifecycleAdmission": ".types",
    "SourceLifecycleState": ".types",
    "SourceLifecycleTransport": ".types",
    "SourceSnapshot": ".types",
    "TransportKeyDeleteResult": ".types",
    "TransportKeyResult": ".types",
    "TransportModeRequestMode": ".types",
    "TransportSnapshot": ".types",
    "TransportSnapshotMode": ".types",
    "UnauthorizedError": ".errors",
    "UnlockResult": ".types",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
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
    "BridgeStatus",
    "ClientSnapshot",
    "ConflictError",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DeleteRecordingResult",
    "DownloadTicket",
    "ErrorDetail",
    "ErrorResponse",
    "FernApi",
    "HttpValidationError",
    "InsufficientStorageError",
    "LevelSnapshot",
    "NotFoundError",
    "RecordingCapabilities",
    "RecordingFormat",
    "RecordingFormatCodec",
    "RecordingFormatContainer",
    "RecordingLimits",
    "RecordingList",
    "RecordingResult",
    "RecordingSnapshot",
    "RecordingSnapshotSource",
    "RecordingSnapshotSourceTwo",
    "RecordingSnapshotState",
    "RecordingStorage",
    "ServiceUnavailableError",
    "SourceLifecycle",
    "SourceLifecycleAdmission",
    "SourceLifecycleState",
    "SourceLifecycleTransport",
    "SourceSnapshot",
    "TransportKeyDeleteResult",
    "TransportKeyResult",
    "TransportModeRequestMode",
    "TransportSnapshot",
    "TransportSnapshotMode",
    "UnauthorizedError",
    "UnlockResult",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
]
