



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_system_info_response import GetSystemInfoResponse
    from .get_system_info_response_device import GetSystemInfoResponseDevice
    from .get_system_info_response_meter import GetSystemInfoResponseMeter
    from .get_system_info_response_wifi import GetSystemInfoResponseWifi
_dynamic_imports: typing.Dict[str, str] = {
    "GetSystemInfoResponse": ".get_system_info_response",
    "GetSystemInfoResponseDevice": ".get_system_info_response_device",
    "GetSystemInfoResponseMeter": ".get_system_info_response_meter",
    "GetSystemInfoResponseWifi": ".get_system_info_response_wifi",
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
    "GetSystemInfoResponse",
    "GetSystemInfoResponseDevice",
    "GetSystemInfoResponseMeter",
    "GetSystemInfoResponseWifi",
]
