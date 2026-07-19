



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        MetadataGetStatusResponse,
        MetadataGetUserResponse,
        MetadataRetrieveCurrentBalancesResponse,
        MetadataSendFeedbackRequestFeature,
        MetadataSendFeedbackResponse,
        MetadataSendTelemetryRequestEventsItem,
        MetadataSendTelemetryRequestEventsItemError,
        MetadataSendTelemetryRequestEventsItemErrorData,
        MetadataSendTelemetryRequestEventsItemSessionEnd,
        MetadataSendTelemetryRequestEventsItemSessionEndData,
        MetadataSendTelemetryRequestEventsItemSessionStart,
        MetadataSendTelemetryRequestEventsItemSessionStartData,
        MetadataSendTelemetryRequestEventsItemToolUsage,
        MetadataSendTelemetryRequestEventsItemToolUsageData,
        MetadataSendTelemetryRequestEventsItemUserInput,
        MetadataSendTelemetryRequestEventsItemUserInputData,
        MetadataSendTelemetryRequestEventsItem_Error,
        MetadataSendTelemetryRequestEventsItem_SessionEnd,
        MetadataSendTelemetryRequestEventsItem_SessionStart,
        MetadataSendTelemetryRequestEventsItem_ToolUsage,
        MetadataSendTelemetryRequestEventsItem_UserInput,
        MetadataSendTelemetryRequestService,
        MetadataSendTelemetryResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "MetadataGetStatusResponse": ".types",
    "MetadataGetUserResponse": ".types",
    "MetadataRetrieveCurrentBalancesResponse": ".types",
    "MetadataSendFeedbackRequestFeature": ".types",
    "MetadataSendFeedbackResponse": ".types",
    "MetadataSendTelemetryRequestEventsItem": ".types",
    "MetadataSendTelemetryRequestEventsItemError": ".types",
    "MetadataSendTelemetryRequestEventsItemErrorData": ".types",
    "MetadataSendTelemetryRequestEventsItemSessionEnd": ".types",
    "MetadataSendTelemetryRequestEventsItemSessionEndData": ".types",
    "MetadataSendTelemetryRequestEventsItemSessionStart": ".types",
    "MetadataSendTelemetryRequestEventsItemSessionStartData": ".types",
    "MetadataSendTelemetryRequestEventsItemToolUsage": ".types",
    "MetadataSendTelemetryRequestEventsItemToolUsageData": ".types",
    "MetadataSendTelemetryRequestEventsItemUserInput": ".types",
    "MetadataSendTelemetryRequestEventsItemUserInputData": ".types",
    "MetadataSendTelemetryRequestEventsItem_Error": ".types",
    "MetadataSendTelemetryRequestEventsItem_SessionEnd": ".types",
    "MetadataSendTelemetryRequestEventsItem_SessionStart": ".types",
    "MetadataSendTelemetryRequestEventsItem_ToolUsage": ".types",
    "MetadataSendTelemetryRequestEventsItem_UserInput": ".types",
    "MetadataSendTelemetryRequestService": ".types",
    "MetadataSendTelemetryResponse": ".types",
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
