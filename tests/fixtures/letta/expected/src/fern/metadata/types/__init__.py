



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .metadata_get_status_response import MetadataGetStatusResponse
    from .metadata_get_user_response import MetadataGetUserResponse
    from .metadata_retrieve_current_balances_response import MetadataRetrieveCurrentBalancesResponse
    from .metadata_send_feedback_request_feature import MetadataSendFeedbackRequestFeature
    from .metadata_send_feedback_response import MetadataSendFeedbackResponse
    from .metadata_send_telemetry_request_events_item import (
        MetadataSendTelemetryRequestEventsItem,
        MetadataSendTelemetryRequestEventsItem_Error,
        MetadataSendTelemetryRequestEventsItem_SessionEnd,
        MetadataSendTelemetryRequestEventsItem_SessionStart,
        MetadataSendTelemetryRequestEventsItem_ToolUsage,
        MetadataSendTelemetryRequestEventsItem_UserInput,
    )
    from .metadata_send_telemetry_request_events_item_error import MetadataSendTelemetryRequestEventsItemError
    from .metadata_send_telemetry_request_events_item_error_data import MetadataSendTelemetryRequestEventsItemErrorData
    from .metadata_send_telemetry_request_events_item_session_end import (
        MetadataSendTelemetryRequestEventsItemSessionEnd,
    )
    from .metadata_send_telemetry_request_events_item_session_end_data import (
        MetadataSendTelemetryRequestEventsItemSessionEndData,
    )
    from .metadata_send_telemetry_request_events_item_session_start import (
        MetadataSendTelemetryRequestEventsItemSessionStart,
    )
    from .metadata_send_telemetry_request_events_item_session_start_data import (
        MetadataSendTelemetryRequestEventsItemSessionStartData,
    )
    from .metadata_send_telemetry_request_events_item_tool_usage import MetadataSendTelemetryRequestEventsItemToolUsage
    from .metadata_send_telemetry_request_events_item_tool_usage_data import (
        MetadataSendTelemetryRequestEventsItemToolUsageData,
    )
    from .metadata_send_telemetry_request_events_item_user_input import MetadataSendTelemetryRequestEventsItemUserInput
    from .metadata_send_telemetry_request_events_item_user_input_data import (
        MetadataSendTelemetryRequestEventsItemUserInputData,
    )
    from .metadata_send_telemetry_request_service import MetadataSendTelemetryRequestService
    from .metadata_send_telemetry_response import MetadataSendTelemetryResponse
_dynamic_imports: typing.Dict[str, str] = {
    "MetadataGetStatusResponse": ".metadata_get_status_response",
    "MetadataGetUserResponse": ".metadata_get_user_response",
    "MetadataRetrieveCurrentBalancesResponse": ".metadata_retrieve_current_balances_response",
    "MetadataSendFeedbackRequestFeature": ".metadata_send_feedback_request_feature",
    "MetadataSendFeedbackResponse": ".metadata_send_feedback_response",
    "MetadataSendTelemetryRequestEventsItem": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestEventsItemError": ".metadata_send_telemetry_request_events_item_error",
    "MetadataSendTelemetryRequestEventsItemErrorData": ".metadata_send_telemetry_request_events_item_error_data",
    "MetadataSendTelemetryRequestEventsItemSessionEnd": ".metadata_send_telemetry_request_events_item_session_end",
    "MetadataSendTelemetryRequestEventsItemSessionEndData": ".metadata_send_telemetry_request_events_item_session_end_data",
    "MetadataSendTelemetryRequestEventsItemSessionStart": ".metadata_send_telemetry_request_events_item_session_start",
    "MetadataSendTelemetryRequestEventsItemSessionStartData": ".metadata_send_telemetry_request_events_item_session_start_data",
    "MetadataSendTelemetryRequestEventsItemToolUsage": ".metadata_send_telemetry_request_events_item_tool_usage",
    "MetadataSendTelemetryRequestEventsItemToolUsageData": ".metadata_send_telemetry_request_events_item_tool_usage_data",
    "MetadataSendTelemetryRequestEventsItemUserInput": ".metadata_send_telemetry_request_events_item_user_input",
    "MetadataSendTelemetryRequestEventsItemUserInputData": ".metadata_send_telemetry_request_events_item_user_input_data",
    "MetadataSendTelemetryRequestEventsItem_Error": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestEventsItem_SessionEnd": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestEventsItem_SessionStart": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestEventsItem_ToolUsage": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestEventsItem_UserInput": ".metadata_send_telemetry_request_events_item",
    "MetadataSendTelemetryRequestService": ".metadata_send_telemetry_request_service",
    "MetadataSendTelemetryResponse": ".metadata_send_telemetry_response",
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
    "MetadataGetStatusResponse",
    "MetadataGetUserResponse",
    "MetadataRetrieveCurrentBalancesResponse",
    "MetadataSendFeedbackRequestFeature",
    "MetadataSendFeedbackResponse",
    "MetadataSendTelemetryRequestEventsItem",
    "MetadataSendTelemetryRequestEventsItemError",
    "MetadataSendTelemetryRequestEventsItemErrorData",
    "MetadataSendTelemetryRequestEventsItemSessionEnd",
    "MetadataSendTelemetryRequestEventsItemSessionEndData",
    "MetadataSendTelemetryRequestEventsItemSessionStart",
    "MetadataSendTelemetryRequestEventsItemSessionStartData",
    "MetadataSendTelemetryRequestEventsItemToolUsage",
    "MetadataSendTelemetryRequestEventsItemToolUsageData",
    "MetadataSendTelemetryRequestEventsItemUserInput",
    "MetadataSendTelemetryRequestEventsItemUserInputData",
    "MetadataSendTelemetryRequestEventsItem_Error",
    "MetadataSendTelemetryRequestEventsItem_SessionEnd",
    "MetadataSendTelemetryRequestEventsItem_SessionStart",
    "MetadataSendTelemetryRequestEventsItem_ToolUsage",
    "MetadataSendTelemetryRequestEventsItem_UserInput",
    "MetadataSendTelemetryRequestService",
    "MetadataSendTelemetryResponse",
]
