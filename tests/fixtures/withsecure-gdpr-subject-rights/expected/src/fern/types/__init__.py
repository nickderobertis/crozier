



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .context_description import ContextDescription
    from .context_uuid import ContextUuid
    from .contexts_response import ContextsResponse
    from .contexts_response_item import ContextsResponseItem
    from .custom_identifier import CustomIdentifier
    from .deletion_denied_reason import DeletionDeniedReason
    from .deletion_denied_response import DeletionDeniedResponse
    from .deletion_ready_response import DeletionReadyResponse
    from .deletion_ready_response_deletion_feedback import DeletionReadyResponseDeletionFeedback
    from .deletion_request_grounds import DeletionRequestGrounds
    from .deletion_request_response import DeletionRequestResponse
    from .deletion_request_uuid import DeletionRequestUuid
    from .email_address import EmailAddress
    from .export_partial_ready_response import ExportPartialReadyResponse
    from .export_ready_response import ExportReadyResponse
    from .export_request_response import ExportRequestResponse
    from .export_request_uuid import ExportRequestUuid
    from .government_id_number import GovernmentIdNumber
    from .required_auth import RequiredAuth
    from .required_auth_item_item import RequiredAuthItemItem
    from .supplied_auth import SuppliedAuth
    from .supplied_auth_custom_identifier import SuppliedAuthCustomIdentifier
    from .supplied_auth_government_id_number import SuppliedAuthGovernmentIdNumber
    from .telephone_number import TelephoneNumber
_dynamic_imports: typing.Dict[str, str] = {
    "ContextDescription": ".context_description",
    "ContextUuid": ".context_uuid",
    "ContextsResponse": ".contexts_response",
    "ContextsResponseItem": ".contexts_response_item",
    "CustomIdentifier": ".custom_identifier",
    "DeletionDeniedReason": ".deletion_denied_reason",
    "DeletionDeniedResponse": ".deletion_denied_response",
    "DeletionReadyResponse": ".deletion_ready_response",
    "DeletionReadyResponseDeletionFeedback": ".deletion_ready_response_deletion_feedback",
    "DeletionRequestGrounds": ".deletion_request_grounds",
    "DeletionRequestResponse": ".deletion_request_response",
    "DeletionRequestUuid": ".deletion_request_uuid",
    "EmailAddress": ".email_address",
    "ExportPartialReadyResponse": ".export_partial_ready_response",
    "ExportReadyResponse": ".export_ready_response",
    "ExportRequestResponse": ".export_request_response",
    "ExportRequestUuid": ".export_request_uuid",
    "GovernmentIdNumber": ".government_id_number",
    "RequiredAuth": ".required_auth",
    "RequiredAuthItemItem": ".required_auth_item_item",
    "SuppliedAuth": ".supplied_auth",
    "SuppliedAuthCustomIdentifier": ".supplied_auth_custom_identifier",
    "SuppliedAuthGovernmentIdNumber": ".supplied_auth_government_id_number",
    "TelephoneNumber": ".telephone_number",
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
    "ContextDescription",
    "ContextUuid",
    "ContextsResponse",
    "ContextsResponseItem",
    "CustomIdentifier",
    "DeletionDeniedReason",
    "DeletionDeniedResponse",
    "DeletionReadyResponse",
    "DeletionReadyResponseDeletionFeedback",
    "DeletionRequestGrounds",
    "DeletionRequestResponse",
    "DeletionRequestUuid",
    "EmailAddress",
    "ExportPartialReadyResponse",
    "ExportReadyResponse",
    "ExportRequestResponse",
    "ExportRequestUuid",
    "GovernmentIdNumber",
    "RequiredAuth",
    "RequiredAuthItemItem",
    "SuppliedAuth",
    "SuppliedAuthCustomIdentifier",
    "SuppliedAuthGovernmentIdNumber",
    "TelephoneNumber",
]
