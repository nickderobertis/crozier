



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_device_to_fleets_response import AddDeviceToFleetsResponse
    from .delete_device_from_fleets_response import DeleteDeviceFromFleetsResponse
    from .delete_firmware_request_firmware_type import DeleteFirmwareRequestFirmwareType
    from .download_firmware_request_firmware_type import DownloadFirmwareRequestFirmwareType
    from .get_device_dfu_history_request_firmware_type import GetDeviceDfuHistoryRequestFirmwareType
    from .get_device_dfu_status_request_firmware_type import GetDeviceDfuStatusRequestFirmwareType
    from .get_device_fleets_response import GetDeviceFleetsResponse
    from .get_devices_dfu_history_request_firmware_type import GetDevicesDfuHistoryRequestFirmwareType
    from .get_devices_dfu_history_request_sort_by import GetDevicesDfuHistoryRequestSortBy
    from .get_devices_dfu_history_request_sort_order import GetDevicesDfuHistoryRequestSortOrder
    from .get_devices_dfu_status_request_firmware_type import GetDevicesDfuStatusRequestFirmwareType
    from .get_devices_dfu_status_request_sort_by import GetDevicesDfuStatusRequestSortBy
    from .get_devices_dfu_status_request_sort_order import GetDevicesDfuStatusRequestSortOrder
    from .get_firmware_info_request_sort_by import GetFirmwareInfoRequestSortBy
    from .get_firmware_info_request_sort_order import GetFirmwareInfoRequestSortOrder
    from .get_fleets_response import GetFleetsResponse
    from .get_products_response import GetProductsResponse
    from .get_project_members_response import GetProjectMembersResponse
    from .get_projects_response import GetProjectsResponse
    from .perform_dfu_action_request_action import PerformDfuActionRequestAction
    from .perform_dfu_action_request_firmware_type import PerformDfuActionRequestFirmwareType
    from .update_firmware_request_firmware_type import UpdateFirmwareRequestFirmwareType
    from .upload_firmware_request_firmware_type import UploadFirmwareRequestFirmwareType
_dynamic_imports: typing.Dict[str, str] = {
    "AddDeviceToFleetsResponse": ".add_device_to_fleets_response",
    "DeleteDeviceFromFleetsResponse": ".delete_device_from_fleets_response",
    "DeleteFirmwareRequestFirmwareType": ".delete_firmware_request_firmware_type",
    "DownloadFirmwareRequestFirmwareType": ".download_firmware_request_firmware_type",
    "GetDeviceDfuHistoryRequestFirmwareType": ".get_device_dfu_history_request_firmware_type",
    "GetDeviceDfuStatusRequestFirmwareType": ".get_device_dfu_status_request_firmware_type",
    "GetDeviceFleetsResponse": ".get_device_fleets_response",
    "GetDevicesDfuHistoryRequestFirmwareType": ".get_devices_dfu_history_request_firmware_type",
    "GetDevicesDfuHistoryRequestSortBy": ".get_devices_dfu_history_request_sort_by",
    "GetDevicesDfuHistoryRequestSortOrder": ".get_devices_dfu_history_request_sort_order",
    "GetDevicesDfuStatusRequestFirmwareType": ".get_devices_dfu_status_request_firmware_type",
    "GetDevicesDfuStatusRequestSortBy": ".get_devices_dfu_status_request_sort_by",
    "GetDevicesDfuStatusRequestSortOrder": ".get_devices_dfu_status_request_sort_order",
    "GetFirmwareInfoRequestSortBy": ".get_firmware_info_request_sort_by",
    "GetFirmwareInfoRequestSortOrder": ".get_firmware_info_request_sort_order",
    "GetFleetsResponse": ".get_fleets_response",
    "GetProductsResponse": ".get_products_response",
    "GetProjectMembersResponse": ".get_project_members_response",
    "GetProjectsResponse": ".get_projects_response",
    "PerformDfuActionRequestAction": ".perform_dfu_action_request_action",
    "PerformDfuActionRequestFirmwareType": ".perform_dfu_action_request_firmware_type",
    "UpdateFirmwareRequestFirmwareType": ".update_firmware_request_firmware_type",
    "UploadFirmwareRequestFirmwareType": ".upload_firmware_request_firmware_type",
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
    "AddDeviceToFleetsResponse",
    "DeleteDeviceFromFleetsResponse",
    "DeleteFirmwareRequestFirmwareType",
    "DownloadFirmwareRequestFirmwareType",
    "GetDeviceDfuHistoryRequestFirmwareType",
    "GetDeviceDfuStatusRequestFirmwareType",
    "GetDeviceFleetsResponse",
    "GetDevicesDfuHistoryRequestFirmwareType",
    "GetDevicesDfuHistoryRequestSortBy",
    "GetDevicesDfuHistoryRequestSortOrder",
    "GetDevicesDfuStatusRequestFirmwareType",
    "GetDevicesDfuStatusRequestSortBy",
    "GetDevicesDfuStatusRequestSortOrder",
    "GetFirmwareInfoRequestSortBy",
    "GetFirmwareInfoRequestSortOrder",
    "GetFleetsResponse",
    "GetProductsResponse",
    "GetProjectMembersResponse",
    "GetProjectsResponse",
    "PerformDfuActionRequestAction",
    "PerformDfuActionRequestFirmwareType",
    "UpdateFirmwareRequestFirmwareType",
    "UploadFirmwareRequestFirmwareType",
]
