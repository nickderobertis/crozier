



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .affected_agent import AffectedAgent
    from .agent_delegation import AgentDelegation
    from .agent_detail import AgentDetail
    from .approval_detail_response import ApprovalDetailResponse
    from .approval_error import ApprovalError
    from .approval_pair import ApprovalPair
    from .approval_sync_response import ApprovalSyncResponse
    from .approval_sync_response_data import ApprovalSyncResponseData
    from .approve_response import ApproveResponse
    from .approve_response_data import ApproveResponseData
    from .approve_response_data_persistence import ApproveResponseDataPersistence
    from .approve_response_data_status import ApproveResponseDataStatus
    from .available_service import AvailableService
    from .cimd_metadata import CimdMetadata
    from .consume_response import ConsumeResponse
    from .consume_response_data import ConsumeResponseData
    from .create_approval_response import CreateApprovalResponse
    from .create_approval_response_data import CreateApprovalResponseData
    from .create_approval_response_data_status import CreateApprovalResponseDataStatus
    from .create_or_update_grant_response import CreateOrUpdateGrantResponse
    from .delegated_token import DelegatedToken
    from .deny_response import DenyResponse
    from .deny_response_data import DenyResponseData
    from .deny_response_data_persistence import DenyResponseDataPersistence
    from .deny_response_data_status import DenyResponseDataStatus
    from .error import Error
    from .error_response import ErrorResponse
    from .get_agent_delegations_response import GetAgentDelegationsResponse
    from .get_agent_detail_response import GetAgentDetailResponse
    from .get_agent_detail_response_data import GetAgentDetailResponseData
    from .get_agent_grants_response import GetAgentGrantsResponse
    from .get_user_info_response import GetUserInfoResponse
    from .health_response import HealthResponse
    from .health_response_status import HealthResponseStatus
    from .internal_server_error_body import InternalServerErrorBody
    from .jwk_set_response import JwkSetResponse
    from .jwk_set_response_keys_item import JwkSetResponseKeysItem
    from .jwk_set_response_keys_item_use import JwkSetResponseKeysItemUse
    from .o_auth2error import OAuth2Error
    from .o_auth2error_error import OAuth2ErrorError
    from .o_auth2error_response import OAuth2ErrorResponse
    from .o_auth2error_response_error import OAuth2ErrorResponseError
    from .o_auth2metadata_response import OAuth2MetadataResponse
    from .o_auth2token_response import OAuth2TokenResponse
    from .o_auth2token_response_token_type import OAuth2TokenResponseTokenType
    from .o_auth_scope import OAuthScope
    from .permission_set_with_requirement import PermissionSetWithRequirement
    from .permission_set_with_requirement_permission_set import PermissionSetWithRequirementPermissionSet
    from .permission_set_with_requirement_permission_set_service_scopes_item import (
        PermissionSetWithRequirementPermissionSetServiceScopesItem,
    )
    from .permission_set_with_requirement_permission_set_service_scopes_item_requirement_type import (
        PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType,
    )
    from .permission_set_with_requirement_requirement_type import PermissionSetWithRequirementRequirementType
    from .scope_preview_response import ScopePreviewResponse
    from .scope_preview_response_data import ScopePreviewResponseData
    from .scope_with_description import ScopeWithDescription
    from .service_requirement_for_user import ServiceRequirementForUser
    from .service_requirement_for_user_connection_status import ServiceRequirementForUserConnectionStatus
    from .service_requirement_for_user_requirement_type import ServiceRequirementForUserRequirementType
    from .service_scope import ServiceScope
    from .service_unavailable_error_body import ServiceUnavailableErrorBody
    from .session_status import SessionStatus
    from .third_party_service import ThirdPartyService
    from .third_party_service_with_session import ThirdPartyServiceWithSession
    from .thirdparty_service import ThirdpartyService
    from .token_exchange_request import TokenExchangeRequest
    from .token_exchange_request_actor_token_type import TokenExchangeRequestActorTokenType
    from .token_exchange_request_client_assertion_type import TokenExchangeRequestClientAssertionType
    from .token_exchange_request_grant_type import TokenExchangeRequestGrantType
    from .token_exchange_request_requested_token_type import TokenExchangeRequestRequestedTokenType
    from .token_exchange_response import TokenExchangeResponse
    from .tool_approval_detail import ToolApprovalDetail
    from .tool_approval_detail_persistence import ToolApprovalDetailPersistence
    from .tool_approval_detail_risk_level import ToolApprovalDetailRiskLevel
    from .tool_approval_detail_status import ToolApprovalDetailStatus
    from .tool_approval_summary import ToolApprovalSummary
    from .tool_approval_summary_persistence import ToolApprovalSummaryPersistence
    from .tool_approval_summary_status import ToolApprovalSummaryStatus
    from .user_grant import UserGrant
    from .user_info import UserInfo
    from .user_session_summary import UserSessionSummary
_dynamic_imports: typing.Dict[str, str] = {
    "AffectedAgent": ".affected_agent",
    "AgentDelegation": ".agent_delegation",
    "AgentDetail": ".agent_detail",
    "ApprovalDetailResponse": ".approval_detail_response",
    "ApprovalError": ".approval_error",
    "ApprovalPair": ".approval_pair",
    "ApprovalSyncResponse": ".approval_sync_response",
    "ApprovalSyncResponseData": ".approval_sync_response_data",
    "ApproveResponse": ".approve_response",
    "ApproveResponseData": ".approve_response_data",
    "ApproveResponseDataPersistence": ".approve_response_data_persistence",
    "ApproveResponseDataStatus": ".approve_response_data_status",
    "AvailableService": ".available_service",
    "CimdMetadata": ".cimd_metadata",
    "ConsumeResponse": ".consume_response",
    "ConsumeResponseData": ".consume_response_data",
    "CreateApprovalResponse": ".create_approval_response",
    "CreateApprovalResponseData": ".create_approval_response_data",
    "CreateApprovalResponseDataStatus": ".create_approval_response_data_status",
    "CreateOrUpdateGrantResponse": ".create_or_update_grant_response",
    "DelegatedToken": ".delegated_token",
    "DenyResponse": ".deny_response",
    "DenyResponseData": ".deny_response_data",
    "DenyResponseDataPersistence": ".deny_response_data_persistence",
    "DenyResponseDataStatus": ".deny_response_data_status",
    "Error": ".error",
    "ErrorResponse": ".error_response",
    "GetAgentDelegationsResponse": ".get_agent_delegations_response",
    "GetAgentDetailResponse": ".get_agent_detail_response",
    "GetAgentDetailResponseData": ".get_agent_detail_response_data",
    "GetAgentGrantsResponse": ".get_agent_grants_response",
    "GetUserInfoResponse": ".get_user_info_response",
    "HealthResponse": ".health_response",
    "HealthResponseStatus": ".health_response_status",
    "InternalServerErrorBody": ".internal_server_error_body",
    "JwkSetResponse": ".jwk_set_response",
    "JwkSetResponseKeysItem": ".jwk_set_response_keys_item",
    "JwkSetResponseKeysItemUse": ".jwk_set_response_keys_item_use",
    "OAuth2Error": ".o_auth2error",
    "OAuth2ErrorError": ".o_auth2error_error",
    "OAuth2ErrorResponse": ".o_auth2error_response",
    "OAuth2ErrorResponseError": ".o_auth2error_response_error",
    "OAuth2MetadataResponse": ".o_auth2metadata_response",
    "OAuth2TokenResponse": ".o_auth2token_response",
    "OAuth2TokenResponseTokenType": ".o_auth2token_response_token_type",
    "OAuthScope": ".o_auth_scope",
    "PermissionSetWithRequirement": ".permission_set_with_requirement",
    "PermissionSetWithRequirementPermissionSet": ".permission_set_with_requirement_permission_set",
    "PermissionSetWithRequirementPermissionSetServiceScopesItem": ".permission_set_with_requirement_permission_set_service_scopes_item",
    "PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType": ".permission_set_with_requirement_permission_set_service_scopes_item_requirement_type",
    "PermissionSetWithRequirementRequirementType": ".permission_set_with_requirement_requirement_type",
    "ScopePreviewResponse": ".scope_preview_response",
    "ScopePreviewResponseData": ".scope_preview_response_data",
    "ScopeWithDescription": ".scope_with_description",
    "ServiceRequirementForUser": ".service_requirement_for_user",
    "ServiceRequirementForUserConnectionStatus": ".service_requirement_for_user_connection_status",
    "ServiceRequirementForUserRequirementType": ".service_requirement_for_user_requirement_type",
    "ServiceScope": ".service_scope",
    "ServiceUnavailableErrorBody": ".service_unavailable_error_body",
    "SessionStatus": ".session_status",
    "ThirdPartyService": ".third_party_service",
    "ThirdPartyServiceWithSession": ".third_party_service_with_session",
    "ThirdpartyService": ".thirdparty_service",
    "TokenExchangeRequest": ".token_exchange_request",
    "TokenExchangeRequestActorTokenType": ".token_exchange_request_actor_token_type",
    "TokenExchangeRequestClientAssertionType": ".token_exchange_request_client_assertion_type",
    "TokenExchangeRequestGrantType": ".token_exchange_request_grant_type",
    "TokenExchangeRequestRequestedTokenType": ".token_exchange_request_requested_token_type",
    "TokenExchangeResponse": ".token_exchange_response",
    "ToolApprovalDetail": ".tool_approval_detail",
    "ToolApprovalDetailPersistence": ".tool_approval_detail_persistence",
    "ToolApprovalDetailRiskLevel": ".tool_approval_detail_risk_level",
    "ToolApprovalDetailStatus": ".tool_approval_detail_status",
    "ToolApprovalSummary": ".tool_approval_summary",
    "ToolApprovalSummaryPersistence": ".tool_approval_summary_persistence",
    "ToolApprovalSummaryStatus": ".tool_approval_summary_status",
    "UserGrant": ".user_grant",
    "UserInfo": ".user_info",
    "UserSessionSummary": ".user_session_summary",
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
    "AffectedAgent",
    "AgentDelegation",
    "AgentDetail",
    "ApprovalDetailResponse",
    "ApprovalError",
    "ApprovalPair",
    "ApprovalSyncResponse",
    "ApprovalSyncResponseData",
    "ApproveResponse",
    "ApproveResponseData",
    "ApproveResponseDataPersistence",
    "ApproveResponseDataStatus",
    "AvailableService",
    "CimdMetadata",
    "ConsumeResponse",
    "ConsumeResponseData",
    "CreateApprovalResponse",
    "CreateApprovalResponseData",
    "CreateApprovalResponseDataStatus",
    "CreateOrUpdateGrantResponse",
    "DelegatedToken",
    "DenyResponse",
    "DenyResponseData",
    "DenyResponseDataPersistence",
    "DenyResponseDataStatus",
    "Error",
    "ErrorResponse",
    "GetAgentDelegationsResponse",
    "GetAgentDetailResponse",
    "GetAgentDetailResponseData",
    "GetAgentGrantsResponse",
    "GetUserInfoResponse",
    "HealthResponse",
    "HealthResponseStatus",
    "InternalServerErrorBody",
    "JwkSetResponse",
    "JwkSetResponseKeysItem",
    "JwkSetResponseKeysItemUse",
    "OAuth2Error",
    "OAuth2ErrorError",
    "OAuth2ErrorResponse",
    "OAuth2ErrorResponseError",
    "OAuth2MetadataResponse",
    "OAuth2TokenResponse",
    "OAuth2TokenResponseTokenType",
    "OAuthScope",
    "PermissionSetWithRequirement",
    "PermissionSetWithRequirementPermissionSet",
    "PermissionSetWithRequirementPermissionSetServiceScopesItem",
    "PermissionSetWithRequirementPermissionSetServiceScopesItemRequirementType",
    "PermissionSetWithRequirementRequirementType",
    "ScopePreviewResponse",
    "ScopePreviewResponseData",
    "ScopeWithDescription",
    "ServiceRequirementForUser",
    "ServiceRequirementForUserConnectionStatus",
    "ServiceRequirementForUserRequirementType",
    "ServiceScope",
    "ServiceUnavailableErrorBody",
    "SessionStatus",
    "ThirdPartyService",
    "ThirdPartyServiceWithSession",
    "ThirdpartyService",
    "TokenExchangeRequest",
    "TokenExchangeRequestActorTokenType",
    "TokenExchangeRequestClientAssertionType",
    "TokenExchangeRequestGrantType",
    "TokenExchangeRequestRequestedTokenType",
    "TokenExchangeResponse",
    "ToolApprovalDetail",
    "ToolApprovalDetailPersistence",
    "ToolApprovalDetailRiskLevel",
    "ToolApprovalDetailStatus",
    "ToolApprovalSummary",
    "ToolApprovalSummaryPersistence",
    "ToolApprovalSummaryStatus",
    "UserGrant",
    "UserInfo",
    "UserSessionSummary",
]
