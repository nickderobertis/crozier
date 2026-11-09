



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_edit_delete_license_decision_response import AddEditDeleteLicenseDecisionResponse
    from .create_upload_request_location import CreateUploadRequestLocation
    from .get_item_tree_view_request_sort import GetItemTreeViewRequestSort
    from .get_licenses_by_upload_id_request_agent_item import GetLicensesByUploadIdRequestAgentItem
    from .get_previous_and_next_item_request_selection import GetPreviousAndNextItemRequestSelection
    from .get_uploads_request_status import GetUploadsRequestStatus
    from .move_upload_by_id_request_action import MoveUploadByIdRequestAction
    from .schedule_bulk_scan_bulk_actions_item import ScheduleBulkScanBulkActionsItem
    from .schedule_bulk_scan_bulk_actions_item_license_action import ScheduleBulkScanBulkActionsItemLicenseAction
    from .schedule_bulk_scan_bulk_scope import ScheduleBulkScanBulkScope
    from .set_upload_permissions_request_new_permission import SetUploadPermissionsRequestNewPermission
    from .set_upload_permissions_request_public_permission import SetUploadPermissionsRequestPublicPermission
    from .update_upload_by_id_request_status import UpdateUploadByIdRequestStatus
_dynamic_imports: typing.Dict[str, str] = {
    "AddEditDeleteLicenseDecisionResponse": ".add_edit_delete_license_decision_response",
    "CreateUploadRequestLocation": ".create_upload_request_location",
    "GetItemTreeViewRequestSort": ".get_item_tree_view_request_sort",
    "GetLicensesByUploadIdRequestAgentItem": ".get_licenses_by_upload_id_request_agent_item",
    "GetPreviousAndNextItemRequestSelection": ".get_previous_and_next_item_request_selection",
    "GetUploadsRequestStatus": ".get_uploads_request_status",
    "MoveUploadByIdRequestAction": ".move_upload_by_id_request_action",
    "ScheduleBulkScanBulkActionsItem": ".schedule_bulk_scan_bulk_actions_item",
    "ScheduleBulkScanBulkActionsItemLicenseAction": ".schedule_bulk_scan_bulk_actions_item_license_action",
    "ScheduleBulkScanBulkScope": ".schedule_bulk_scan_bulk_scope",
    "SetUploadPermissionsRequestNewPermission": ".set_upload_permissions_request_new_permission",
    "SetUploadPermissionsRequestPublicPermission": ".set_upload_permissions_request_public_permission",
    "UpdateUploadByIdRequestStatus": ".update_upload_by_id_request_status",
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
