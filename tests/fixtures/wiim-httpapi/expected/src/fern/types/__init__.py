



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bluetooth_device_list import BluetoothDeviceList
    from .bluetooth_device_list_list_item import BluetoothDeviceListListItem
    from .device_debug_info import DeviceDebugInfo
    from .device_status import DeviceStatus
    from .player_status import PlayerStatus
    from .player_status_status import PlayerStatusStatus
    from .preset_list import PresetList
    from .preset_list_preset_list_item import PresetListPresetListItem
    from .static_ip_info import StaticIpInfo
    from .track_metadata import TrackMetadata
    from .track_metadata_meta_data import TrackMetadataMetaData
_dynamic_imports: typing.Dict[str, str] = {
    "BluetoothDeviceList": ".bluetooth_device_list",
    "BluetoothDeviceListListItem": ".bluetooth_device_list_list_item",
    "DeviceDebugInfo": ".device_debug_info",
    "DeviceStatus": ".device_status",
    "PlayerStatus": ".player_status",
    "PlayerStatusStatus": ".player_status_status",
    "PresetList": ".preset_list",
    "PresetListPresetListItem": ".preset_list_preset_list_item",
    "StaticIpInfo": ".static_ip_info",
    "TrackMetadata": ".track_metadata",
    "TrackMetadataMetaData": ".track_metadata_meta_data",
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
    "BluetoothDeviceList",
    "BluetoothDeviceListListItem",
    "DeviceDebugInfo",
    "DeviceStatus",
    "PlayerStatus",
    "PlayerStatusStatus",
    "PresetList",
    "PresetListPresetListItem",
    "StaticIpInfo",
    "TrackMetadata",
    "TrackMetadataMetaData",
]
