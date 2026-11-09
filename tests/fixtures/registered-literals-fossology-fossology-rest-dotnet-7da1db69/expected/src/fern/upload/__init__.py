



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AddEditDeleteLicenseDecisionResponse,
        CreateUploadRequestLocation,
        GetItemTreeViewRequestSort,
        GetLicensesByUploadIdRequestAgentItem,
        GetPreviousAndNextItemRequestSelection,
        GetUploadsRequestStatus,
        MoveUploadByIdRequestAction,
        ScheduleBulkScanBulkActionsItem,
        ScheduleBulkScanBulkActionsItemLicenseAction,
        ScheduleBulkScanBulkScope,
        SetUploadPermissionsRequestNewPermission,
        SetUploadPermissionsRequestPublicPermission,
        UpdateUploadByIdRequestStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AddEditDeleteLicenseDecisionResponse": ".types",
    "CreateUploadRequestLocation": ".types",
    "GetItemTreeViewRequestSort": ".types",
    "GetLicensesByUploadIdRequestAgentItem": ".types",
    "GetPreviousAndNextItemRequestSelection": ".types",
    "GetUploadsRequestStatus": ".types",
    "MoveUploadByIdRequestAction": ".types",
    "ScheduleBulkScanBulkActionsItem": ".types",
    "ScheduleBulkScanBulkActionsItemLicenseAction": ".types",
    "ScheduleBulkScanBulkScope": ".types",
    "SetUploadPermissionsRequestNewPermission": ".types",
    "SetUploadPermissionsRequestPublicPermission": ".types",
    "UpdateUploadByIdRequestStatus": ".types",
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
    "AddEditDeleteLicenseDecisionResponse",
    "CreateUploadRequestLocation",
    "GetItemTreeViewRequestSort",
    "GetLicensesByUploadIdRequestAgentItem",
    "GetPreviousAndNextItemRequestSelection",
    "GetUploadsRequestStatus",
    "MoveUploadByIdRequestAction",
    "ScheduleBulkScanBulkActionsItem",
    "ScheduleBulkScanBulkActionsItemLicenseAction",
    "ScheduleBulkScanBulkScope",
    "SetUploadPermissionsRequestNewPermission",
    "SetUploadPermissionsRequestPublicPermission",
    "UpdateUploadByIdRequestStatus",
]
