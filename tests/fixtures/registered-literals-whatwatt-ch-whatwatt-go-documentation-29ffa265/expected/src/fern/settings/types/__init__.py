



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_settings_response import GetSettingsResponse
    from .get_settings_response_services import GetSettingsResponseServices
    from .get_settings_response_services_berry import GetSettingsResponseServicesBerry
    from .get_settings_response_services_cloud import GetSettingsResponseServicesCloud
    from .get_settings_response_services_local import GetSettingsResponseServicesLocal
    from .get_settings_response_services_modbus import GetSettingsResponseServicesModbus
    from .get_settings_response_services_sd import GetSettingsResponseServicesSd
    from .get_settings_response_system import GetSettingsResponseSystem
    from .replace_settings_request_services import ReplaceSettingsRequestServices
    from .replace_settings_request_services_berry import ReplaceSettingsRequestServicesBerry
    from .replace_settings_request_services_cloud import ReplaceSettingsRequestServicesCloud
    from .replace_settings_request_services_local import ReplaceSettingsRequestServicesLocal
    from .replace_settings_request_services_modbus import ReplaceSettingsRequestServicesModbus
    from .replace_settings_request_services_sd import ReplaceSettingsRequestServicesSd
    from .replace_settings_request_system import ReplaceSettingsRequestSystem
    from .replace_settings_response import ReplaceSettingsResponse
    from .replace_settings_response_services import ReplaceSettingsResponseServices
    from .replace_settings_response_services_berry import ReplaceSettingsResponseServicesBerry
    from .replace_settings_response_services_cloud import ReplaceSettingsResponseServicesCloud
    from .replace_settings_response_services_local import ReplaceSettingsResponseServicesLocal
    from .replace_settings_response_services_modbus import ReplaceSettingsResponseServicesModbus
    from .replace_settings_response_services_sd import ReplaceSettingsResponseServicesSd
    from .replace_settings_response_system import ReplaceSettingsResponseSystem
    from .update_settings_request_services import UpdateSettingsRequestServices
    from .update_settings_request_services_berry import UpdateSettingsRequestServicesBerry
    from .update_settings_request_services_cloud import UpdateSettingsRequestServicesCloud
    from .update_settings_request_services_local import UpdateSettingsRequestServicesLocal
    from .update_settings_request_services_modbus import UpdateSettingsRequestServicesModbus
    from .update_settings_request_services_sd import UpdateSettingsRequestServicesSd
    from .update_settings_request_system import UpdateSettingsRequestSystem
    from .update_settings_response import UpdateSettingsResponse
    from .update_settings_response_services import UpdateSettingsResponseServices
    from .update_settings_response_services_berry import UpdateSettingsResponseServicesBerry
    from .update_settings_response_services_cloud import UpdateSettingsResponseServicesCloud
    from .update_settings_response_services_local import UpdateSettingsResponseServicesLocal
    from .update_settings_response_services_modbus import UpdateSettingsResponseServicesModbus
    from .update_settings_response_services_sd import UpdateSettingsResponseServicesSd
    from .update_settings_response_system import UpdateSettingsResponseSystem
_dynamic_imports: typing.Dict[str, str] = {
    "GetSettingsResponse": ".get_settings_response",
    "GetSettingsResponseServices": ".get_settings_response_services",
    "GetSettingsResponseServicesBerry": ".get_settings_response_services_berry",
    "GetSettingsResponseServicesCloud": ".get_settings_response_services_cloud",
    "GetSettingsResponseServicesLocal": ".get_settings_response_services_local",
    "GetSettingsResponseServicesModbus": ".get_settings_response_services_modbus",
    "GetSettingsResponseServicesSd": ".get_settings_response_services_sd",
    "GetSettingsResponseSystem": ".get_settings_response_system",
    "ReplaceSettingsRequestServices": ".replace_settings_request_services",
    "ReplaceSettingsRequestServicesBerry": ".replace_settings_request_services_berry",
    "ReplaceSettingsRequestServicesCloud": ".replace_settings_request_services_cloud",
    "ReplaceSettingsRequestServicesLocal": ".replace_settings_request_services_local",
    "ReplaceSettingsRequestServicesModbus": ".replace_settings_request_services_modbus",
    "ReplaceSettingsRequestServicesSd": ".replace_settings_request_services_sd",
    "ReplaceSettingsRequestSystem": ".replace_settings_request_system",
    "ReplaceSettingsResponse": ".replace_settings_response",
    "ReplaceSettingsResponseServices": ".replace_settings_response_services",
    "ReplaceSettingsResponseServicesBerry": ".replace_settings_response_services_berry",
    "ReplaceSettingsResponseServicesCloud": ".replace_settings_response_services_cloud",
    "ReplaceSettingsResponseServicesLocal": ".replace_settings_response_services_local",
    "ReplaceSettingsResponseServicesModbus": ".replace_settings_response_services_modbus",
    "ReplaceSettingsResponseServicesSd": ".replace_settings_response_services_sd",
    "ReplaceSettingsResponseSystem": ".replace_settings_response_system",
    "UpdateSettingsRequestServices": ".update_settings_request_services",
    "UpdateSettingsRequestServicesBerry": ".update_settings_request_services_berry",
    "UpdateSettingsRequestServicesCloud": ".update_settings_request_services_cloud",
    "UpdateSettingsRequestServicesLocal": ".update_settings_request_services_local",
    "UpdateSettingsRequestServicesModbus": ".update_settings_request_services_modbus",
    "UpdateSettingsRequestServicesSd": ".update_settings_request_services_sd",
    "UpdateSettingsRequestSystem": ".update_settings_request_system",
    "UpdateSettingsResponse": ".update_settings_response",
    "UpdateSettingsResponseServices": ".update_settings_response_services",
    "UpdateSettingsResponseServicesBerry": ".update_settings_response_services_berry",
    "UpdateSettingsResponseServicesCloud": ".update_settings_response_services_cloud",
    "UpdateSettingsResponseServicesLocal": ".update_settings_response_services_local",
    "UpdateSettingsResponseServicesModbus": ".update_settings_response_services_modbus",
    "UpdateSettingsResponseServicesSd": ".update_settings_response_services_sd",
    "UpdateSettingsResponseSystem": ".update_settings_response_system",
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
    "GetSettingsResponse",
    "GetSettingsResponseServices",
    "GetSettingsResponseServicesBerry",
    "GetSettingsResponseServicesCloud",
    "GetSettingsResponseServicesLocal",
    "GetSettingsResponseServicesModbus",
    "GetSettingsResponseServicesSd",
    "GetSettingsResponseSystem",
    "ReplaceSettingsRequestServices",
    "ReplaceSettingsRequestServicesBerry",
    "ReplaceSettingsRequestServicesCloud",
    "ReplaceSettingsRequestServicesLocal",
    "ReplaceSettingsRequestServicesModbus",
    "ReplaceSettingsRequestServicesSd",
    "ReplaceSettingsRequestSystem",
    "ReplaceSettingsResponse",
    "ReplaceSettingsResponseServices",
    "ReplaceSettingsResponseServicesBerry",
    "ReplaceSettingsResponseServicesCloud",
    "ReplaceSettingsResponseServicesLocal",
    "ReplaceSettingsResponseServicesModbus",
    "ReplaceSettingsResponseServicesSd",
    "ReplaceSettingsResponseSystem",
    "UpdateSettingsRequestServices",
    "UpdateSettingsRequestServicesBerry",
    "UpdateSettingsRequestServicesCloud",
    "UpdateSettingsRequestServicesLocal",
    "UpdateSettingsRequestServicesModbus",
    "UpdateSettingsRequestServicesSd",
    "UpdateSettingsRequestSystem",
    "UpdateSettingsResponse",
    "UpdateSettingsResponseServices",
    "UpdateSettingsResponseServicesBerry",
    "UpdateSettingsResponseServicesCloud",
    "UpdateSettingsResponseServicesLocal",
    "UpdateSettingsResponseServicesModbus",
    "UpdateSettingsResponseServicesSd",
    "UpdateSettingsResponseSystem",
]
