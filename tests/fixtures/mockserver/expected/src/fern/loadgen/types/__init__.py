



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_mockserver_load_scenario_name_response import DeleteMockserverLoadScenarioNameResponse
    from .delete_mockserver_load_scenario_name_response_status import DeleteMockserverLoadScenarioNameResponseStatus
    from .delete_mockserver_load_scenario_response import DeleteMockserverLoadScenarioResponse
    from .delete_mockserver_load_scenario_response_status import DeleteMockserverLoadScenarioResponseStatus
    from .get_mockserver_load_scenario_name_report_request_format import (
        GetMockserverLoadScenarioNameReportRequestFormat,
    )
    from .get_mockserver_load_scenario_response import GetMockserverLoadScenarioResponse
    from .put_mockserver_load_scenario_generate_from_open_api_request_target import (
        PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget,
    )
    from .put_mockserver_load_scenario_generate_from_open_api_request_target_scheme import (
        PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme,
    )
    from .put_mockserver_load_scenario_generate_from_open_api_response import (
        PutMockserverLoadScenarioGenerateFromOpenApiResponse,
    )
    from .put_mockserver_load_scenario_generate_from_open_api_response_state import (
        PutMockserverLoadScenarioGenerateFromOpenApiResponseState,
    )
    from .put_mockserver_load_scenario_generate_from_open_api_response_status import (
        PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus,
    )
    from .put_mockserver_load_scenario_generate_from_recording_request_mode import (
        PutMockserverLoadScenarioGenerateFromRecordingRequestMode,
    )
    from .put_mockserver_load_scenario_generate_from_recording_request_target import (
        PutMockserverLoadScenarioGenerateFromRecordingRequestTarget,
    )
    from .put_mockserver_load_scenario_generate_from_recording_request_target_scheme import (
        PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme,
    )
    from .put_mockserver_load_scenario_generate_from_recording_response import (
        PutMockserverLoadScenarioGenerateFromRecordingResponse,
    )
    from .put_mockserver_load_scenario_generate_from_recording_response_state import (
        PutMockserverLoadScenarioGenerateFromRecordingResponseState,
    )
    from .put_mockserver_load_scenario_generate_from_recording_response_status import (
        PutMockserverLoadScenarioGenerateFromRecordingResponseStatus,
    )
    from .put_mockserver_load_scenario_response import PutMockserverLoadScenarioResponse
    from .put_mockserver_load_scenario_response_state import PutMockserverLoadScenarioResponseState
    from .put_mockserver_load_scenario_response_status import PutMockserverLoadScenarioResponseStatus
    from .put_mockserver_load_scenario_start_response import PutMockserverLoadScenarioStartResponse
    from .put_mockserver_load_scenario_start_response_started_item import (
        PutMockserverLoadScenarioStartResponseStartedItem,
    )
    from .put_mockserver_load_scenario_start_response_started_item_state import (
        PutMockserverLoadScenarioStartResponseStartedItemState,
    )
    from .put_mockserver_load_scenario_start_response_status import PutMockserverLoadScenarioStartResponseStatus
    from .put_mockserver_load_scenario_stop_response import PutMockserverLoadScenarioStopResponse
    from .put_mockserver_load_scenario_stop_response_status import PutMockserverLoadScenarioStopResponseStatus
    from .put_mockserver_load_scenario_stop_response_stopped_item import (
        PutMockserverLoadScenarioStopResponseStoppedItem,
    )
    from .put_mockserver_load_scenario_stop_response_stopped_item_state import (
        PutMockserverLoadScenarioStopResponseStoppedItemState,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteMockserverLoadScenarioNameResponse": ".delete_mockserver_load_scenario_name_response",
    "DeleteMockserverLoadScenarioNameResponseStatus": ".delete_mockserver_load_scenario_name_response_status",
    "DeleteMockserverLoadScenarioResponse": ".delete_mockserver_load_scenario_response",
    "DeleteMockserverLoadScenarioResponseStatus": ".delete_mockserver_load_scenario_response_status",
    "GetMockserverLoadScenarioNameReportRequestFormat": ".get_mockserver_load_scenario_name_report_request_format",
    "GetMockserverLoadScenarioResponse": ".get_mockserver_load_scenario_response",
    "PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget": ".put_mockserver_load_scenario_generate_from_open_api_request_target",
    "PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme": ".put_mockserver_load_scenario_generate_from_open_api_request_target_scheme",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponse": ".put_mockserver_load_scenario_generate_from_open_api_response",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponseState": ".put_mockserver_load_scenario_generate_from_open_api_response_state",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus": ".put_mockserver_load_scenario_generate_from_open_api_response_status",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestMode": ".put_mockserver_load_scenario_generate_from_recording_request_mode",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestTarget": ".put_mockserver_load_scenario_generate_from_recording_request_target",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme": ".put_mockserver_load_scenario_generate_from_recording_request_target_scheme",
    "PutMockserverLoadScenarioGenerateFromRecordingResponse": ".put_mockserver_load_scenario_generate_from_recording_response",
    "PutMockserverLoadScenarioGenerateFromRecordingResponseState": ".put_mockserver_load_scenario_generate_from_recording_response_state",
    "PutMockserverLoadScenarioGenerateFromRecordingResponseStatus": ".put_mockserver_load_scenario_generate_from_recording_response_status",
    "PutMockserverLoadScenarioResponse": ".put_mockserver_load_scenario_response",
    "PutMockserverLoadScenarioResponseState": ".put_mockserver_load_scenario_response_state",
    "PutMockserverLoadScenarioResponseStatus": ".put_mockserver_load_scenario_response_status",
    "PutMockserverLoadScenarioStartResponse": ".put_mockserver_load_scenario_start_response",
    "PutMockserverLoadScenarioStartResponseStartedItem": ".put_mockserver_load_scenario_start_response_started_item",
    "PutMockserverLoadScenarioStartResponseStartedItemState": ".put_mockserver_load_scenario_start_response_started_item_state",
    "PutMockserverLoadScenarioStartResponseStatus": ".put_mockserver_load_scenario_start_response_status",
    "PutMockserverLoadScenarioStopResponse": ".put_mockserver_load_scenario_stop_response",
    "PutMockserverLoadScenarioStopResponseStatus": ".put_mockserver_load_scenario_stop_response_status",
    "PutMockserverLoadScenarioStopResponseStoppedItem": ".put_mockserver_load_scenario_stop_response_stopped_item",
    "PutMockserverLoadScenarioStopResponseStoppedItemState": ".put_mockserver_load_scenario_stop_response_stopped_item_state",
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
    "DeleteMockserverLoadScenarioNameResponse",
    "DeleteMockserverLoadScenarioNameResponseStatus",
    "DeleteMockserverLoadScenarioResponse",
    "DeleteMockserverLoadScenarioResponseStatus",
    "GetMockserverLoadScenarioNameReportRequestFormat",
    "GetMockserverLoadScenarioResponse",
    "PutMockserverLoadScenarioGenerateFromOpenApiRequestTarget",
    "PutMockserverLoadScenarioGenerateFromOpenApiRequestTargetScheme",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponse",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponseState",
    "PutMockserverLoadScenarioGenerateFromOpenApiResponseStatus",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestMode",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestTarget",
    "PutMockserverLoadScenarioGenerateFromRecordingRequestTargetScheme",
    "PutMockserverLoadScenarioGenerateFromRecordingResponse",
    "PutMockserverLoadScenarioGenerateFromRecordingResponseState",
    "PutMockserverLoadScenarioGenerateFromRecordingResponseStatus",
    "PutMockserverLoadScenarioResponse",
    "PutMockserverLoadScenarioResponseState",
    "PutMockserverLoadScenarioResponseStatus",
    "PutMockserverLoadScenarioStartResponse",
    "PutMockserverLoadScenarioStartResponseStartedItem",
    "PutMockserverLoadScenarioStartResponseStartedItemState",
    "PutMockserverLoadScenarioStartResponseStatus",
    "PutMockserverLoadScenarioStopResponse",
    "PutMockserverLoadScenarioStopResponseStatus",
    "PutMockserverLoadScenarioStopResponseStoppedItem",
    "PutMockserverLoadScenarioStopResponseStoppedItemState",
]
