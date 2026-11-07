



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workflows_list_all_request_status import WorkflowsListAllRequestStatus
    from .workflows_revert_to_review_request_user import WorkflowsRevertToReviewRequestUser
    from .workflows_update_approval_status_request_status import WorkflowsUpdateApprovalStatusRequestStatus
    from .workflows_update_approval_status_request_user import WorkflowsUpdateApprovalStatusRequestUser
    from .workflows_update_metadata_request_updates_item import WorkflowsUpdateMetadataRequestUpdatesItem
    from .workflows_update_metadata_request_updates_item_action import WorkflowsUpdateMetadataRequestUpdatesItemAction
_dynamic_imports: typing.Dict[str, str] = {
    "WorkflowsListAllRequestStatus": ".workflows_list_all_request_status",
    "WorkflowsRevertToReviewRequestUser": ".workflows_revert_to_review_request_user",
    "WorkflowsUpdateApprovalStatusRequestStatus": ".workflows_update_approval_status_request_status",
    "WorkflowsUpdateApprovalStatusRequestUser": ".workflows_update_approval_status_request_user",
    "WorkflowsUpdateMetadataRequestUpdatesItem": ".workflows_update_metadata_request_updates_item",
    "WorkflowsUpdateMetadataRequestUpdatesItemAction": ".workflows_update_metadata_request_updates_item_action",
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
    "WorkflowsListAllRequestStatus",
    "WorkflowsRevertToReviewRequestUser",
    "WorkflowsUpdateApprovalStatusRequestStatus",
    "WorkflowsUpdateApprovalStatusRequestUser",
    "WorkflowsUpdateMetadataRequestUpdatesItem",
    "WorkflowsUpdateMetadataRequestUpdatesItemAction",
]
