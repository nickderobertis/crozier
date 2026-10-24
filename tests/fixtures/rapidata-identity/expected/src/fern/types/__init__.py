



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .accept_org_invitation_by_id_endpoint_output import AcceptOrgInvitationByIdEndpointOutput
    from .accept_org_invitation_endpoint_output import AcceptOrgInvitationEndpointOutput
    from .authorization_relations_bidder import AuthorizationRelationsBidder
    from .authorization_relations_external_app import AuthorizationRelationsExternalApp
    from .authorization_relations_platform import AuthorizationRelationsPlatform
    from .authorization_scope import AuthorizationScope
    from .capability import Capability
    from .client import Client
    from .create_bridge_token_endpoint_output import CreateBridgeTokenEndpointOutput
    from .create_client_endpoint_output import CreateClientEndpointOutput
    from .create_organization_endpoint_output import CreateOrganizationEndpointOutput
    from .external_app_id import ExternalAppId
    from .get_bidder_relation_members_endpoint_cursor_paged_result_of_output import (
        GetBidderRelationMembersEndpointCursorPagedResultOfOutput,
    )
    from .get_bidder_relation_members_endpoint_output import GetBidderRelationMembersEndpointOutput
    from .get_capability_grantees_endpoint_cursor_paged_result_of_output import (
        GetCapabilityGranteesEndpointCursorPagedResultOfOutput,
    )
    from .get_capability_grantees_endpoint_output import GetCapabilityGranteesEndpointOutput
    from .get_clients_request_client_id import GetClientsRequestClientId
    from .get_clients_request_created_at import GetClientsRequestCreatedAt
    from .get_clients_request_display_name import GetClientsRequestDisplayName
    from .get_customer_capabilities_endpoint_output import GetCustomerCapabilitiesEndpointOutput
    from .get_customers_request_email import GetCustomersRequestEmail
    from .get_customers_request_id import GetCustomersRequestId
    from .get_customers_request_organization_id import GetCustomersRequestOrganizationId
    from .get_customers_request_organization_name import GetCustomersRequestOrganizationName
    from .get_external_app_relation_members_endpoint_cursor_paged_result_of_output import (
        GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput,
    )
    from .get_external_app_relation_members_endpoint_output import GetExternalAppRelationMembersEndpointOutput
    from .get_organization_capabilities_endpoint_output import GetOrganizationCapabilitiesEndpointOutput
    from .get_organization_endpoint_output import GetOrganizationEndpointOutput
    from .get_organizations_all_request_id import GetOrganizationsAllRequestId
    from .get_organizations_all_request_name import GetOrganizationsAllRequestName
    from .get_organizations_all_request_owner_email import GetOrganizationsAllRequestOwnerEmail
    from .get_organizations_request_id import GetOrganizationsRequestId
    from .get_organizations_request_name import GetOrganizationsRequestName
    from .get_platform_relation_members_endpoint_cursor_paged_result_of_output import (
        GetPlatformRelationMembersEndpointCursorPagedResultOfOutput,
    )
    from .get_platform_relation_members_endpoint_output import GetPlatformRelationMembersEndpointOutput
    from .google_one_tap_login_endpoint_output import GoogleOneTapLoginEndpointOutput
    from .invite_org_member_endpoint_output import InviteOrgMemberEndpointOutput
    from .json_web_key import JsonWebKey
    from .json_web_key_set import JsonWebKeySet
    from .list_my_org_invitations_endpoint_output import ListMyOrgInvitationsEndpointOutput
    from .list_my_org_invitations_endpoint_output_invitation import ListMyOrgInvitationsEndpointOutputInvitation
    from .list_org_invitations_endpoint_output import ListOrgInvitationsEndpointOutput
    from .list_org_invitations_endpoint_output_invitation import ListOrgInvitationsEndpointOutputInvitation
    from .list_org_members_endpoint_output import ListOrgMembersEndpointOutput
    from .list_org_members_endpoint_output_member import ListOrgMembersEndpointOutputMember
    from .membership_status import MembershipStatus
    from .org_role import OrgRole
    from .query_all_organizations_endpoint_output import QueryAllOrganizationsEndpointOutput
    from .query_all_organizations_endpoint_paged_result_of_output import (
        QueryAllOrganizationsEndpointPagedResultOfOutput,
    )
    from .query_clients_endpoint_output import QueryClientsEndpointOutput
    from .query_clients_endpoint_paged_result_of_output import QueryClientsEndpointPagedResultOfOutput
    from .query_customers_endpoint_output import QueryCustomersEndpointOutput
    from .query_customers_endpoint_paged_result_of_output import QueryCustomersEndpointPagedResultOfOutput
    from .query_organizations_endpoint_output import QueryOrganizationsEndpointOutput
    from .query_organizations_endpoint_paged_result_of_output import QueryOrganizationsEndpointPagedResultOfOutput
    from .read_bridge_token_endpoint_keys_output import ReadBridgeTokenEndpointKeysOutput
    from .read_bridge_token_endpoint_not_available_output import ReadBridgeTokenEndpointNotAvailableOutput
    from .validation_problem_details import ValidationProblemDetails
_dynamic_imports: typing.Dict[str, str] = {
    "AcceptOrgInvitationByIdEndpointOutput": ".accept_org_invitation_by_id_endpoint_output",
    "AcceptOrgInvitationEndpointOutput": ".accept_org_invitation_endpoint_output",
    "AuthorizationRelationsBidder": ".authorization_relations_bidder",
    "AuthorizationRelationsExternalApp": ".authorization_relations_external_app",
    "AuthorizationRelationsPlatform": ".authorization_relations_platform",
    "AuthorizationScope": ".authorization_scope",
    "Capability": ".capability",
    "Client": ".client",
    "CreateBridgeTokenEndpointOutput": ".create_bridge_token_endpoint_output",
    "CreateClientEndpointOutput": ".create_client_endpoint_output",
    "CreateOrganizationEndpointOutput": ".create_organization_endpoint_output",
    "ExternalAppId": ".external_app_id",
    "GetBidderRelationMembersEndpointCursorPagedResultOfOutput": ".get_bidder_relation_members_endpoint_cursor_paged_result_of_output",
    "GetBidderRelationMembersEndpointOutput": ".get_bidder_relation_members_endpoint_output",
    "GetCapabilityGranteesEndpointCursorPagedResultOfOutput": ".get_capability_grantees_endpoint_cursor_paged_result_of_output",
    "GetCapabilityGranteesEndpointOutput": ".get_capability_grantees_endpoint_output",
    "GetClientsRequestClientId": ".get_clients_request_client_id",
    "GetClientsRequestCreatedAt": ".get_clients_request_created_at",
    "GetClientsRequestDisplayName": ".get_clients_request_display_name",
    "GetCustomerCapabilitiesEndpointOutput": ".get_customer_capabilities_endpoint_output",
    "GetCustomersRequestEmail": ".get_customers_request_email",
    "GetCustomersRequestId": ".get_customers_request_id",
    "GetCustomersRequestOrganizationId": ".get_customers_request_organization_id",
    "GetCustomersRequestOrganizationName": ".get_customers_request_organization_name",
    "GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput": ".get_external_app_relation_members_endpoint_cursor_paged_result_of_output",
    "GetExternalAppRelationMembersEndpointOutput": ".get_external_app_relation_members_endpoint_output",
    "GetOrganizationCapabilitiesEndpointOutput": ".get_organization_capabilities_endpoint_output",
    "GetOrganizationEndpointOutput": ".get_organization_endpoint_output",
    "GetOrganizationsAllRequestId": ".get_organizations_all_request_id",
    "GetOrganizationsAllRequestName": ".get_organizations_all_request_name",
    "GetOrganizationsAllRequestOwnerEmail": ".get_organizations_all_request_owner_email",
    "GetOrganizationsRequestId": ".get_organizations_request_id",
    "GetOrganizationsRequestName": ".get_organizations_request_name",
    "GetPlatformRelationMembersEndpointCursorPagedResultOfOutput": ".get_platform_relation_members_endpoint_cursor_paged_result_of_output",
    "GetPlatformRelationMembersEndpointOutput": ".get_platform_relation_members_endpoint_output",
    "GoogleOneTapLoginEndpointOutput": ".google_one_tap_login_endpoint_output",
    "InviteOrgMemberEndpointOutput": ".invite_org_member_endpoint_output",
    "JsonWebKey": ".json_web_key",
    "JsonWebKeySet": ".json_web_key_set",
    "ListMyOrgInvitationsEndpointOutput": ".list_my_org_invitations_endpoint_output",
    "ListMyOrgInvitationsEndpointOutputInvitation": ".list_my_org_invitations_endpoint_output_invitation",
    "ListOrgInvitationsEndpointOutput": ".list_org_invitations_endpoint_output",
    "ListOrgInvitationsEndpointOutputInvitation": ".list_org_invitations_endpoint_output_invitation",
    "ListOrgMembersEndpointOutput": ".list_org_members_endpoint_output",
    "ListOrgMembersEndpointOutputMember": ".list_org_members_endpoint_output_member",
    "MembershipStatus": ".membership_status",
    "OrgRole": ".org_role",
    "QueryAllOrganizationsEndpointOutput": ".query_all_organizations_endpoint_output",
    "QueryAllOrganizationsEndpointPagedResultOfOutput": ".query_all_organizations_endpoint_paged_result_of_output",
    "QueryClientsEndpointOutput": ".query_clients_endpoint_output",
    "QueryClientsEndpointPagedResultOfOutput": ".query_clients_endpoint_paged_result_of_output",
    "QueryCustomersEndpointOutput": ".query_customers_endpoint_output",
    "QueryCustomersEndpointPagedResultOfOutput": ".query_customers_endpoint_paged_result_of_output",
    "QueryOrganizationsEndpointOutput": ".query_organizations_endpoint_output",
    "QueryOrganizationsEndpointPagedResultOfOutput": ".query_organizations_endpoint_paged_result_of_output",
    "ReadBridgeTokenEndpointKeysOutput": ".read_bridge_token_endpoint_keys_output",
    "ReadBridgeTokenEndpointNotAvailableOutput": ".read_bridge_token_endpoint_not_available_output",
    "ValidationProblemDetails": ".validation_problem_details",
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
    "AcceptOrgInvitationByIdEndpointOutput",
    "AcceptOrgInvitationEndpointOutput",
    "AuthorizationRelationsBidder",
    "AuthorizationRelationsExternalApp",
    "AuthorizationRelationsPlatform",
    "AuthorizationScope",
    "Capability",
    "Client",
    "CreateBridgeTokenEndpointOutput",
    "CreateClientEndpointOutput",
    "CreateOrganizationEndpointOutput",
    "ExternalAppId",
    "GetBidderRelationMembersEndpointCursorPagedResultOfOutput",
    "GetBidderRelationMembersEndpointOutput",
    "GetCapabilityGranteesEndpointCursorPagedResultOfOutput",
    "GetCapabilityGranteesEndpointOutput",
    "GetClientsRequestClientId",
    "GetClientsRequestCreatedAt",
    "GetClientsRequestDisplayName",
    "GetCustomerCapabilitiesEndpointOutput",
    "GetCustomersRequestEmail",
    "GetCustomersRequestId",
    "GetCustomersRequestOrganizationId",
    "GetCustomersRequestOrganizationName",
    "GetExternalAppRelationMembersEndpointCursorPagedResultOfOutput",
    "GetExternalAppRelationMembersEndpointOutput",
    "GetOrganizationCapabilitiesEndpointOutput",
    "GetOrganizationEndpointOutput",
    "GetOrganizationsAllRequestId",
    "GetOrganizationsAllRequestName",
    "GetOrganizationsAllRequestOwnerEmail",
    "GetOrganizationsRequestId",
    "GetOrganizationsRequestName",
    "GetPlatformRelationMembersEndpointCursorPagedResultOfOutput",
    "GetPlatformRelationMembersEndpointOutput",
    "GoogleOneTapLoginEndpointOutput",
    "InviteOrgMemberEndpointOutput",
    "JsonWebKey",
    "JsonWebKeySet",
    "ListMyOrgInvitationsEndpointOutput",
    "ListMyOrgInvitationsEndpointOutputInvitation",
    "ListOrgInvitationsEndpointOutput",
    "ListOrgInvitationsEndpointOutputInvitation",
    "ListOrgMembersEndpointOutput",
    "ListOrgMembersEndpointOutputMember",
    "MembershipStatus",
    "OrgRole",
    "QueryAllOrganizationsEndpointOutput",
    "QueryAllOrganizationsEndpointPagedResultOfOutput",
    "QueryClientsEndpointOutput",
    "QueryClientsEndpointPagedResultOfOutput",
    "QueryCustomersEndpointOutput",
    "QueryCustomersEndpointPagedResultOfOutput",
    "QueryOrganizationsEndpointOutput",
    "QueryOrganizationsEndpointPagedResultOfOutput",
    "ReadBridgeTokenEndpointKeysOutput",
    "ReadBridgeTokenEndpointNotAvailableOutput",
    "ValidationProblemDetails",
]
