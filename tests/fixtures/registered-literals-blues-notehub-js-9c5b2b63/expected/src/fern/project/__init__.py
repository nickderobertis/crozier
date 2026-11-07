



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AddDeviceToFleetsResponse,
        DeleteDeviceFromFleetsResponse,
        DeleteFirmwareRequestFirmwareType,
        DownloadFirmwareRequestFirmwareType,
        GetDeviceDfuHistoryRequestFirmwareType,
        GetDeviceDfuStatusRequestFirmwareType,
        GetDeviceFleetsResponse,
        GetDevicesDfuHistoryRequestFirmwareType,
        GetDevicesDfuHistoryRequestSortBy,
        GetDevicesDfuHistoryRequestSortOrder,
        GetDevicesDfuStatusRequestFirmwareType,
        GetDevicesDfuStatusRequestSortBy,
        GetDevicesDfuStatusRequestSortOrder,
        GetFirmwareInfoRequestSortBy,
        GetFirmwareInfoRequestSortOrder,
        GetFleetsResponse,
        GetProductsResponse,
        GetProjectMembersResponse,
        GetProjectsResponse,
        PerformDfuActionRequestAction,
        PerformDfuActionRequestFirmwareType,
        UpdateFirmwareRequestFirmwareType,
        UploadFirmwareRequestFirmwareType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AddDeviceToFleetsResponse": ".types",
    "DeleteDeviceFromFleetsResponse": ".types",
    "DeleteFirmwareRequestFirmwareType": ".types",
    "DownloadFirmwareRequestFirmwareType": ".types",
    "GetDeviceDfuHistoryRequestFirmwareType": ".types",
    "GetDeviceDfuStatusRequestFirmwareType": ".types",
    "GetDeviceFleetsResponse": ".types",
    "GetDevicesDfuHistoryRequestFirmwareType": ".types",
    "GetDevicesDfuHistoryRequestSortBy": ".types",
    "GetDevicesDfuHistoryRequestSortOrder": ".types",
    "GetDevicesDfuStatusRequestFirmwareType": ".types",
    "GetDevicesDfuStatusRequestSortBy": ".types",
    "GetDevicesDfuStatusRequestSortOrder": ".types",
    "GetFirmwareInfoRequestSortBy": ".types",
    "GetFirmwareInfoRequestSortOrder": ".types",
    "GetFleetsResponse": ".types",
    "GetProductsResponse": ".types",
    "GetProjectMembersResponse": ".types",
    "GetProjectsResponse": ".types",
    "PerformDfuActionRequestAction": ".types",
    "PerformDfuActionRequestFirmwareType": ".types",
    "UpdateFirmwareRequestFirmwareType": ".types",
    "UploadFirmwareRequestFirmwareType": ".types",
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
