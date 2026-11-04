



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_error import ApiError
    from .api_error_code import ApiErrorCode
    from .api_key_presentation import ApiKeyPresentation
    from .api_key_privilege import ApiKeyPrivilege
    from .api_key_privilege_info import ApiKeyPrivilegeInfo
    from .app_info_presentation import AppInfoPresentation
    from .billing_position import BillingPosition
    from .change_log_entry import ChangeLogEntry
    from .change_role_request import ChangeRoleRequest
    from .country import Country
    from .document import Document
    from .guid import Guid
    from .guid_collection import GuidCollection
    from .guid_collection_physical_state import GuidCollectionPhysicalState
    from .guid_collection_type import GuidCollectionType
    from .guid_physical_state import GuidPhysicalState
    from .history_item import HistoryItem
    from .history_item_type import HistoryItemType
    from .id4n import Id4N
    from .id4n_presentation import Id4NPresentation
    from .id4n_presentation_type import Id4NPresentationType
    from .id4n_properties import Id4NProperties
    from .list_of_gs1s import ListOfGs1S
    from .list_of_id4n_properties import ListOfId4NProperties
    from .list_of_id4ns import ListOfId4Ns
    from .organization import Organization
    from .organization_address import OrganizationAddress
    from .organization_user_invitation import OrganizationUserInvitation
    from .paginated_response_of_api_key_presentation import PaginatedResponseOfApiKeyPresentation
    from .paginated_response_of_api_key_privilege import PaginatedResponseOfApiKeyPrivilege
    from .paginated_response_of_api_key_privilege_info import PaginatedResponseOfApiKeyPrivilegeInfo
    from .paginated_response_of_change_log_entry import PaginatedResponseOfChangeLogEntry
    from .paginated_response_of_country import PaginatedResponseOfCountry
    from .paginated_response_of_document import PaginatedResponseOfDocument
    from .paginated_response_of_guid import PaginatedResponseOfGuid
    from .paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
    from .paginated_response_of_history_item import PaginatedResponseOfHistoryItem
    from .paginated_response_of_id4n_presentation import PaginatedResponseOfId4NPresentation
    from .paginated_response_of_organization import PaginatedResponseOfOrganization
    from .paginated_response_of_partner_organization import PaginatedResponseOfPartnerOrganization
    from .paginated_response_of_role import PaginatedResponseOfRole
    from .paginated_response_of_user_presentation import PaginatedResponseOfUserPresentation
    from .paginated_response_of_user_roles import PaginatedResponseOfUserRoles
    from .paginated_response_ofstring import PaginatedResponseOfstring
    from .partner_organization import PartnerOrganization
    from .public_image_presentation import PublicImagePresentation
    from .queue_presentation import QueuePresentation
    from .role import Role
    from .route import Route
    from .routing_file import RoutingFile
    from .routing_options import RoutingOptions
    from .service_costs import ServiceCosts
    from .simple_message_response import SimpleMessageResponse
    from .transfer_send_info import TransferSendInfo
    from .user_presentation import UserPresentation
    from .user_registration_response import UserRegistrationResponse
    from .user_roles import UserRoles
    from .visibility import Visibility
    from .visibility_update import VisibilityUpdate
    from .who_is_response import WhoIsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ApiError": ".api_error",
    "ApiErrorCode": ".api_error_code",
    "ApiKeyPresentation": ".api_key_presentation",
    "ApiKeyPrivilege": ".api_key_privilege",
    "ApiKeyPrivilegeInfo": ".api_key_privilege_info",
    "AppInfoPresentation": ".app_info_presentation",
    "BillingPosition": ".billing_position",
    "ChangeLogEntry": ".change_log_entry",
    "ChangeRoleRequest": ".change_role_request",
    "Country": ".country",
    "Document": ".document",
    "Guid": ".guid",
    "GuidCollection": ".guid_collection",
    "GuidCollectionPhysicalState": ".guid_collection_physical_state",
    "GuidCollectionType": ".guid_collection_type",
    "GuidPhysicalState": ".guid_physical_state",
    "HistoryItem": ".history_item",
    "HistoryItemType": ".history_item_type",
    "Id4N": ".id4n",
    "Id4NPresentation": ".id4n_presentation",
    "Id4NPresentationType": ".id4n_presentation_type",
    "Id4NProperties": ".id4n_properties",
    "ListOfGs1S": ".list_of_gs1s",
    "ListOfId4NProperties": ".list_of_id4n_properties",
    "ListOfId4Ns": ".list_of_id4ns",
    "Organization": ".organization",
    "OrganizationAddress": ".organization_address",
    "OrganizationUserInvitation": ".organization_user_invitation",
    "PaginatedResponseOfApiKeyPresentation": ".paginated_response_of_api_key_presentation",
    "PaginatedResponseOfApiKeyPrivilege": ".paginated_response_of_api_key_privilege",
    "PaginatedResponseOfApiKeyPrivilegeInfo": ".paginated_response_of_api_key_privilege_info",
    "PaginatedResponseOfChangeLogEntry": ".paginated_response_of_change_log_entry",
    "PaginatedResponseOfCountry": ".paginated_response_of_country",
    "PaginatedResponseOfDocument": ".paginated_response_of_document",
    "PaginatedResponseOfGuid": ".paginated_response_of_guid",
    "PaginatedResponseOfGuidCollection": ".paginated_response_of_guid_collection",
    "PaginatedResponseOfHistoryItem": ".paginated_response_of_history_item",
    "PaginatedResponseOfId4NPresentation": ".paginated_response_of_id4n_presentation",
    "PaginatedResponseOfOrganization": ".paginated_response_of_organization",
    "PaginatedResponseOfPartnerOrganization": ".paginated_response_of_partner_organization",
    "PaginatedResponseOfRole": ".paginated_response_of_role",
    "PaginatedResponseOfUserPresentation": ".paginated_response_of_user_presentation",
    "PaginatedResponseOfUserRoles": ".paginated_response_of_user_roles",
    "PaginatedResponseOfstring": ".paginated_response_ofstring",
    "PartnerOrganization": ".partner_organization",
    "PublicImagePresentation": ".public_image_presentation",
    "QueuePresentation": ".queue_presentation",
    "Role": ".role",
    "Route": ".route",
    "RoutingFile": ".routing_file",
    "RoutingOptions": ".routing_options",
    "ServiceCosts": ".service_costs",
    "SimpleMessageResponse": ".simple_message_response",
    "TransferSendInfo": ".transfer_send_info",
    "UserPresentation": ".user_presentation",
    "UserRegistrationResponse": ".user_registration_response",
    "UserRoles": ".user_roles",
    "Visibility": ".visibility",
    "VisibilityUpdate": ".visibility_update",
    "WhoIsResponse": ".who_is_response",
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
    "ApiError",
    "ApiErrorCode",
    "ApiKeyPresentation",
    "ApiKeyPrivilege",
    "ApiKeyPrivilegeInfo",
    "AppInfoPresentation",
    "BillingPosition",
    "ChangeLogEntry",
    "ChangeRoleRequest",
    "Country",
    "Document",
    "Guid",
    "GuidCollection",
    "GuidCollectionPhysicalState",
    "GuidCollectionType",
    "GuidPhysicalState",
    "HistoryItem",
    "HistoryItemType",
    "Id4N",
    "Id4NPresentation",
    "Id4NPresentationType",
    "Id4NProperties",
    "ListOfGs1S",
    "ListOfId4NProperties",
    "ListOfId4Ns",
    "Organization",
    "OrganizationAddress",
    "OrganizationUserInvitation",
    "PaginatedResponseOfApiKeyPresentation",
    "PaginatedResponseOfApiKeyPrivilege",
    "PaginatedResponseOfApiKeyPrivilegeInfo",
    "PaginatedResponseOfChangeLogEntry",
    "PaginatedResponseOfCountry",
    "PaginatedResponseOfDocument",
    "PaginatedResponseOfGuid",
    "PaginatedResponseOfGuidCollection",
    "PaginatedResponseOfHistoryItem",
    "PaginatedResponseOfId4NPresentation",
    "PaginatedResponseOfOrganization",
    "PaginatedResponseOfPartnerOrganization",
    "PaginatedResponseOfRole",
    "PaginatedResponseOfUserPresentation",
    "PaginatedResponseOfUserRoles",
    "PaginatedResponseOfstring",
    "PartnerOrganization",
    "PublicImagePresentation",
    "QueuePresentation",
    "Role",
    "Route",
    "RoutingFile",
    "RoutingOptions",
    "ServiceCosts",
    "SimpleMessageResponse",
    "TransferSendInfo",
    "UserPresentation",
    "UserRegistrationResponse",
    "UserRoles",
    "Visibility",
    "VisibilityUpdate",
    "WhoIsResponse",
]
