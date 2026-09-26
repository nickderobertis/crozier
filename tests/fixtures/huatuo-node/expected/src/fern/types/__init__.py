



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .apis_v1components_error import ApisV1ComponentsError
    from .apis_v1components_error_code import ApisV1ComponentsErrorCode
    from .apis_v1components_error_response import ApisV1ComponentsErrorResponse
    from .apis_v1components_observation_scope import ApisV1ComponentsObservationScope
    from .container_metadata import ContainerMetadata
    from .container_response import ContainerResponse
    from .operation import Operation
    from .operation_kind import OperationKind
    from .operation_outcome import OperationOutcome
    from .operation_response import OperationResponse
    from .operation_status import OperationStatus
    from .operation_terminal import OperationTerminal
    from .profiling_language import ProfilingLanguage
    from .profiling_mode import ProfilingMode
    from .profiling_operation_spec import ProfilingOperationSpec
    from .profiling_type import ProfilingType
    from .tracing_operation_spec import TracingOperationSpec
    from .tracing_type import TracingType
    from .watch_event import WatchEvent
    from .watch_event_data import WatchEventData
    from .watch_event_filters import WatchEventFilters
    from .watch_event_spec_version import WatchEventSpecVersion
_dynamic_imports: typing.Dict[str, str] = {
    "ApisV1ComponentsError": ".apis_v1components_error",
    "ApisV1ComponentsErrorCode": ".apis_v1components_error_code",
    "ApisV1ComponentsErrorResponse": ".apis_v1components_error_response",
    "ApisV1ComponentsObservationScope": ".apis_v1components_observation_scope",
    "ContainerMetadata": ".container_metadata",
    "ContainerResponse": ".container_response",
    "Operation": ".operation",
    "OperationKind": ".operation_kind",
    "OperationOutcome": ".operation_outcome",
    "OperationResponse": ".operation_response",
    "OperationStatus": ".operation_status",
    "OperationTerminal": ".operation_terminal",
    "ProfilingLanguage": ".profiling_language",
    "ProfilingMode": ".profiling_mode",
    "ProfilingOperationSpec": ".profiling_operation_spec",
    "ProfilingType": ".profiling_type",
    "TracingOperationSpec": ".tracing_operation_spec",
    "TracingType": ".tracing_type",
    "WatchEvent": ".watch_event",
    "WatchEventData": ".watch_event_data",
    "WatchEventFilters": ".watch_event_filters",
    "WatchEventSpecVersion": ".watch_event_spec_version",
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
    "ApisV1ComponentsError",
    "ApisV1ComponentsErrorCode",
    "ApisV1ComponentsErrorResponse",
    "ApisV1ComponentsObservationScope",
    "ContainerMetadata",
    "ContainerResponse",
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
    "TracingOperationSpec",
    "TracingType",
    "WatchEvent",
    "WatchEventData",
    "WatchEventFilters",
    "WatchEventSpecVersion",
]
