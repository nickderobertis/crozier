



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .approve_request_persistence import ApproveRequestPersistence
    from .create_approval_request_metadata import CreateApprovalRequestMetadata
    from .create_approval_request_risk_level import CreateApprovalRequestRiskLevel
    from .deny_request_persistence import DenyRequestPersistence
    from .list_pending_approvals_response import ListPendingApprovalsResponse
    from .list_permanent_approvals_response import ListPermanentApprovalsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ApproveRequestPersistence": ".approve_request_persistence",
    "CreateApprovalRequestMetadata": ".create_approval_request_metadata",
    "CreateApprovalRequestRiskLevel": ".create_approval_request_risk_level",
    "DenyRequestPersistence": ".deny_request_persistence",
    "ListPendingApprovalsResponse": ".list_pending_approvals_response",
    "ListPermanentApprovalsResponse": ".list_permanent_approvals_response",
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
    "ApproveRequestPersistence",
    "CreateApprovalRequestMetadata",
    "CreateApprovalRequestRiskLevel",
    "DenyRequestPersistence",
    "ListPendingApprovalsResponse",
    "ListPermanentApprovalsResponse",
]
