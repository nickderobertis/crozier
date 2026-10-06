



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bridge_status import BridgeStatus
    from .client_snapshot import ClientSnapshot
    from .delete_recording_result import DeleteRecordingResult
    from .download_ticket import DownloadTicket
    from .error_detail import ErrorDetail
    from .error_response import ErrorResponse
    from .http_validation_error import HttpValidationError
    from .level_snapshot import LevelSnapshot
    from .recording_capabilities import RecordingCapabilities
    from .recording_format import RecordingFormat
    from .recording_format_codec import RecordingFormatCodec
    from .recording_format_container import RecordingFormatContainer
    from .recording_limits import RecordingLimits
    from .recording_list import RecordingList
    from .recording_result import RecordingResult
    from .recording_snapshot import RecordingSnapshot
    from .recording_snapshot_source import RecordingSnapshotSource
    from .recording_snapshot_source_two import RecordingSnapshotSourceTwo
    from .recording_snapshot_state import RecordingSnapshotState
    from .recording_storage import RecordingStorage
    from .source_lifecycle import SourceLifecycle
    from .source_lifecycle_admission import SourceLifecycleAdmission
    from .source_lifecycle_state import SourceLifecycleState
    from .source_lifecycle_transport import SourceLifecycleTransport
    from .source_snapshot import SourceSnapshot
    from .transport_key_delete_result import TransportKeyDeleteResult
    from .transport_key_result import TransportKeyResult
    from .transport_mode_request_mode import TransportModeRequestMode
    from .transport_snapshot import TransportSnapshot
    from .transport_snapshot_mode import TransportSnapshotMode
    from .unlock_result import UnlockResult
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "BridgeStatus": ".bridge_status",
    "ClientSnapshot": ".client_snapshot",
    "DeleteRecordingResult": ".delete_recording_result",
    "DownloadTicket": ".download_ticket",
    "ErrorDetail": ".error_detail",
    "ErrorResponse": ".error_response",
    "HttpValidationError": ".http_validation_error",
    "LevelSnapshot": ".level_snapshot",
    "RecordingCapabilities": ".recording_capabilities",
    "RecordingFormat": ".recording_format",
    "RecordingFormatCodec": ".recording_format_codec",
    "RecordingFormatContainer": ".recording_format_container",
    "RecordingLimits": ".recording_limits",
    "RecordingList": ".recording_list",
    "RecordingResult": ".recording_result",
    "RecordingSnapshot": ".recording_snapshot",
    "RecordingSnapshotSource": ".recording_snapshot_source",
    "RecordingSnapshotSourceTwo": ".recording_snapshot_source_two",
    "RecordingSnapshotState": ".recording_snapshot_state",
    "RecordingStorage": ".recording_storage",
    "SourceLifecycle": ".source_lifecycle",
    "SourceLifecycleAdmission": ".source_lifecycle_admission",
    "SourceLifecycleState": ".source_lifecycle_state",
    "SourceLifecycleTransport": ".source_lifecycle_transport",
    "SourceSnapshot": ".source_snapshot",
    "TransportKeyDeleteResult": ".transport_key_delete_result",
    "TransportKeyResult": ".transport_key_result",
    "TransportModeRequestMode": ".transport_mode_request_mode",
    "TransportSnapshot": ".transport_snapshot",
    "TransportSnapshotMode": ".transport_snapshot_mode",
    "UnlockResult": ".unlock_result",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "BridgeStatus",
    "ClientSnapshot",
    "DeleteRecordingResult",
    "DownloadTicket",
    "ErrorDetail",
    "ErrorResponse",
    "HttpValidationError",
    "LevelSnapshot",
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
    "UnlockResult",
    "ValidationError",
    "ValidationErrorLocItem",
]
