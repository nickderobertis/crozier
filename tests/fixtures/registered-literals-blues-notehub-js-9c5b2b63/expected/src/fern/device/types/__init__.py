



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_db_note_response import GetDbNoteResponse
    from .get_device_environment_variables_by_pin_response import GetDeviceEnvironmentVariablesByPinResponse
    from .get_device_environment_variables_response import GetDeviceEnvironmentVariablesResponse
    from .get_device_health_log_request_log_type_item import GetDeviceHealthLogRequestLogTypeItem
    from .get_device_health_log_response import GetDeviceHealthLogResponse
    from .get_device_health_log_response_health_log_item import GetDeviceHealthLogResponseHealthLogItem
    from .get_device_journey_response import GetDeviceJourneyResponse
    from .get_device_journey_response_journey import GetDeviceJourneyResponseJourney
    from .get_device_journeys_response import GetDeviceJourneysResponse
    from .get_device_journeys_response_journeys_item import GetDeviceJourneysResponseJourneysItem
    from .get_device_latest_events_response import GetDeviceLatestEventsResponse
    from .get_device_plans_response import GetDevicePlansResponse
    from .get_device_public_key_response import GetDevicePublicKeyResponse
    from .get_device_public_keys_response import GetDevicePublicKeysResponse
    from .get_device_public_keys_response_device_public_keys_item import GetDevicePublicKeysResponseDevicePublicKeysItem
    from .get_device_sessions_response import GetDeviceSessionsResponse
    from .get_devices_response import GetDevicesResponse
    from .get_fleet_devices_response import GetFleetDevicesResponse
    from .get_notefile_response import GetNotefileResponse
    from .signal_device_response import SignalDeviceResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetDbNoteResponse": ".get_db_note_response",
    "GetDeviceEnvironmentVariablesByPinResponse": ".get_device_environment_variables_by_pin_response",
    "GetDeviceEnvironmentVariablesResponse": ".get_device_environment_variables_response",
    "GetDeviceHealthLogRequestLogTypeItem": ".get_device_health_log_request_log_type_item",
    "GetDeviceHealthLogResponse": ".get_device_health_log_response",
    "GetDeviceHealthLogResponseHealthLogItem": ".get_device_health_log_response_health_log_item",
    "GetDeviceJourneyResponse": ".get_device_journey_response",
    "GetDeviceJourneyResponseJourney": ".get_device_journey_response_journey",
    "GetDeviceJourneysResponse": ".get_device_journeys_response",
    "GetDeviceJourneysResponseJourneysItem": ".get_device_journeys_response_journeys_item",
    "GetDeviceLatestEventsResponse": ".get_device_latest_events_response",
    "GetDevicePlansResponse": ".get_device_plans_response",
    "GetDevicePublicKeyResponse": ".get_device_public_key_response",
    "GetDevicePublicKeysResponse": ".get_device_public_keys_response",
    "GetDevicePublicKeysResponseDevicePublicKeysItem": ".get_device_public_keys_response_device_public_keys_item",
    "GetDeviceSessionsResponse": ".get_device_sessions_response",
    "GetDevicesResponse": ".get_devices_response",
    "GetFleetDevicesResponse": ".get_fleet_devices_response",
    "GetNotefileResponse": ".get_notefile_response",
    "SignalDeviceResponse": ".signal_device_response",
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
    "GetDbNoteResponse",
    "GetDeviceEnvironmentVariablesByPinResponse",
    "GetDeviceEnvironmentVariablesResponse",
    "GetDeviceHealthLogRequestLogTypeItem",
    "GetDeviceHealthLogResponse",
    "GetDeviceHealthLogResponseHealthLogItem",
    "GetDeviceJourneyResponse",
    "GetDeviceJourneyResponseJourney",
    "GetDeviceJourneysResponse",
    "GetDeviceJourneysResponseJourneysItem",
    "GetDeviceLatestEventsResponse",
    "GetDevicePlansResponse",
    "GetDevicePublicKeyResponse",
    "GetDevicePublicKeysResponse",
    "GetDevicePublicKeysResponseDevicePublicKeysItem",
    "GetDeviceSessionsResponse",
    "GetDevicesResponse",
    "GetFleetDevicesResponse",
    "GetNotefileResponse",
    "SignalDeviceResponse",
]
