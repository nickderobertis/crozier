

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V2ForbiddenDetailCode(enum.StrEnum):
    """
    Stable cause code for an actionable `403` response.
    """

    INSUFFICIENT_WORKSPACE_ROLE = "INSUFFICIENT_WORKSPACE_ROLE"
    PERSONAL_API_KEYS_DISABLED = "PERSONAL_API_KEYS_DISABLED"
    WORKSPACE_KEY_OPERATION_NOT_PERMITTED = "WORKSPACE_KEY_OPERATION_NOT_PERMITTED"
    PRINCIPAL_KIND_NOT_PERMITTED = "PRINCIPAL_KIND_NOT_PERMITTED"
    ORGANIZATION_MEMBERSHIP_REQUIRED = "ORGANIZATION_MEMBERSHIP_REQUIRED"
    ORGANIZATION_ADMIN_REQUIRED = "ORGANIZATION_ADMIN_REQUIRED"
    ENTERPRISE_PLAN_REQUIRED = "ENTERPRISE_PLAN_REQUIRED"
    ORGANIZATION_PLAN_REQUIRED = "ORGANIZATION_PLAN_REQUIRED"
    AUDIT_LOGS_DISABLED = "AUDIT_LOGS_DISABLED"
    ACCESS_REQUESTS_DISABLED = "ACCESS_REQUESTS_DISABLED"
    ACCESS_REQUEST_ORGANIZATION_REQUIRED = "ACCESS_REQUEST_ORGANIZATION_REQUIRED"
    SKILL_EDITOR_ACCESS_REQUIRED = "SKILL_EDITOR_ACCESS_REQUIRED"
    SECRET_ADMIN_ACCESS_REQUIRED = "SECRET_ADMIN_ACCESS_REQUIRED"
    WORKSPACE_RESOURCE_LIMIT_REACHED = "WORKSPACE_RESOURCE_LIMIT_REACHED"
    PUBLIC_SHARING_NOT_ALLOWED = "PUBLIC_SHARING_NOT_ALLOWED"
    CREDENTIAL_ADMIN_ACCESS_REQUIRED = "CREDENTIAL_ADMIN_ACCESS_REQUIRED"
    MCP_SERVER_URL_NOT_ALLOWED = "MCP_SERVER_URL_NOT_ALLOWED"
    WORKSPACE_PLAN_CAPABILITY_REQUIRED = "WORKSPACE_PLAN_CAPABILITY_REQUIRED"
    CHAT_AUTH_MODE_NOT_PERMITTED = "CHAT_AUTH_MODE_NOT_PERMITTED"
    CONNECTOR_MANAGED_RESOURCE_READ_ONLY = "CONNECTOR_MANAGED_RESOURCE_READ_ONLY"
    PERMISSION_GROUP_CAPABILITY_BLOCKED = "PERMISSION_GROUP_CAPABILITY_BLOCKED"
    INTEGRATION_NOT_ALLOWED = "INTEGRATION_NOT_ALLOWED"
    INSUFFICIENT_SCOPE = "INSUFFICIENT_SCOPE"
    SCIM_MANAGED_MEMBERSHIP = "SCIM_MANAGED_MEMBERSHIP"

    def visit(
        self,
        insufficient_workspace_role: typing.Callable[[], T_Result],
        personal_api_keys_disabled: typing.Callable[[], T_Result],
        workspace_key_operation_not_permitted: typing.Callable[[], T_Result],
        principal_kind_not_permitted: typing.Callable[[], T_Result],
        organization_membership_required: typing.Callable[[], T_Result],
        organization_admin_required: typing.Callable[[], T_Result],
        enterprise_plan_required: typing.Callable[[], T_Result],
        organization_plan_required: typing.Callable[[], T_Result],
        audit_logs_disabled: typing.Callable[[], T_Result],
        access_requests_disabled: typing.Callable[[], T_Result],
        access_request_organization_required: typing.Callable[[], T_Result],
        skill_editor_access_required: typing.Callable[[], T_Result],
        secret_admin_access_required: typing.Callable[[], T_Result],
        workspace_resource_limit_reached: typing.Callable[[], T_Result],
        public_sharing_not_allowed: typing.Callable[[], T_Result],
        credential_admin_access_required: typing.Callable[[], T_Result],
        mcp_server_url_not_allowed: typing.Callable[[], T_Result],
        workspace_plan_capability_required: typing.Callable[[], T_Result],
        chat_auth_mode_not_permitted: typing.Callable[[], T_Result],
        connector_managed_resource_read_only: typing.Callable[[], T_Result],
        permission_group_capability_blocked: typing.Callable[[], T_Result],
        integration_not_allowed: typing.Callable[[], T_Result],
        insufficient_scope: typing.Callable[[], T_Result],
        scim_managed_membership: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V2ForbiddenDetailCode.INSUFFICIENT_WORKSPACE_ROLE:
            return insufficient_workspace_role()
        if self is V2ForbiddenDetailCode.PERSONAL_API_KEYS_DISABLED:
            return personal_api_keys_disabled()
        if self is V2ForbiddenDetailCode.WORKSPACE_KEY_OPERATION_NOT_PERMITTED:
            return workspace_key_operation_not_permitted()
        if self is V2ForbiddenDetailCode.PRINCIPAL_KIND_NOT_PERMITTED:
            return principal_kind_not_permitted()
        if self is V2ForbiddenDetailCode.ORGANIZATION_MEMBERSHIP_REQUIRED:
            return organization_membership_required()
        if self is V2ForbiddenDetailCode.ORGANIZATION_ADMIN_REQUIRED:
            return organization_admin_required()
        if self is V2ForbiddenDetailCode.ENTERPRISE_PLAN_REQUIRED:
            return enterprise_plan_required()
        if self is V2ForbiddenDetailCode.ORGANIZATION_PLAN_REQUIRED:
            return organization_plan_required()
        if self is V2ForbiddenDetailCode.AUDIT_LOGS_DISABLED:
            return audit_logs_disabled()
        if self is V2ForbiddenDetailCode.ACCESS_REQUESTS_DISABLED:
            return access_requests_disabled()
        if self is V2ForbiddenDetailCode.ACCESS_REQUEST_ORGANIZATION_REQUIRED:
            return access_request_organization_required()
        if self is V2ForbiddenDetailCode.SKILL_EDITOR_ACCESS_REQUIRED:
            return skill_editor_access_required()
        if self is V2ForbiddenDetailCode.SECRET_ADMIN_ACCESS_REQUIRED:
            return secret_admin_access_required()
        if self is V2ForbiddenDetailCode.WORKSPACE_RESOURCE_LIMIT_REACHED:
            return workspace_resource_limit_reached()
        if self is V2ForbiddenDetailCode.PUBLIC_SHARING_NOT_ALLOWED:
            return public_sharing_not_allowed()
        if self is V2ForbiddenDetailCode.CREDENTIAL_ADMIN_ACCESS_REQUIRED:
            return credential_admin_access_required()
        if self is V2ForbiddenDetailCode.MCP_SERVER_URL_NOT_ALLOWED:
            return mcp_server_url_not_allowed()
        if self is V2ForbiddenDetailCode.WORKSPACE_PLAN_CAPABILITY_REQUIRED:
            return workspace_plan_capability_required()
        if self is V2ForbiddenDetailCode.CHAT_AUTH_MODE_NOT_PERMITTED:
            return chat_auth_mode_not_permitted()
        if self is V2ForbiddenDetailCode.CONNECTOR_MANAGED_RESOURCE_READ_ONLY:
            return connector_managed_resource_read_only()
        if self is V2ForbiddenDetailCode.PERMISSION_GROUP_CAPABILITY_BLOCKED:
            return permission_group_capability_blocked()
        if self is V2ForbiddenDetailCode.INTEGRATION_NOT_ALLOWED:
            return integration_not_allowed()
        if self is V2ForbiddenDetailCode.INSUFFICIENT_SCOPE:
            return insufficient_scope()
        if self is V2ForbiddenDetailCode.SCIM_MANAGED_MEMBERSHIP:
            return scim_managed_membership()
