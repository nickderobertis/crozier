



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address_info import AddressInfo
    from .alert import Alert
    from .alert_list import AlertList
    from .device import Device
    from .device_list import DeviceList
    from .link import Link
    from .service_provider import ServiceProvider
    from .service_provider_list import ServiceProviderList
    from .session import Session
    from .session_list import SessionList
    from .sparkplug_name import SparkplugName
    from .uuid_list import UuidList
_dynamic_imports: typing.Dict[str, str] = {
    "AddressInfo": ".address_info",
    "Alert": ".alert",
    "AlertList": ".alert_list",
    "Device": ".device",
    "DeviceList": ".device_list",
    "Link": ".link",
    "ServiceProvider": ".service_provider",
    "ServiceProviderList": ".service_provider_list",
    "Session": ".session",
    "SessionList": ".session_list",
    "SparkplugName": ".sparkplug_name",
    "UuidList": ".uuid_list",
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
    "AddressInfo",
    "Alert",
    "AlertList",
    "Device",
    "DeviceList",
    "Link",
    "ServiceProvider",
    "ServiceProviderList",
    "Session",
    "SessionList",
    "SparkplugName",
    "UuidList",
]
