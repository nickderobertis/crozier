

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuditAction(enum.StrEnum):
    RBAC_ROLE_GRANTED = "rbac.role_granted"
    RBAC_MEMBER_REMOVED = "rbac.member_removed"
    RBAC_ROLE_CREATED = "rbac.role_created"
    RBAC_ROLE_UPDATED = "rbac.role_updated"
    RBAC_ROLE_DELETED = "rbac.role_deleted"
    RBAC_INVITATION_CREATED = "rbac.invitation_created"
    RBAC_INVITATION_REVOKED = "rbac.invitation_revoked"
    RBAC_INVITATION_ACCEPTED = "rbac.invitation_accepted"
    AUTH_LOGIN_SUCCESS = "auth.login_success"
    AUTH_LOGIN_FAILED = "auth.login_failed"
    AUTH_LOGOUT = "auth.logout"
    AUTH_PASSWORD_CHANGED = "auth.password_changed"
    AUTH_USER_REGISTERED = "auth.user_registered"
    INTEGRATION_CONNECTED = "integration.connected"
    INTEGRATION_DISCONNECTED = "integration.disconnected"
    INTEGRATION_TOKEN_ROTATED = "integration.token_rotated"
    INTEGRATION_TOKEN_DECRYPTED = "integration.token_decrypted"
    INTEGRATION_METADATA_UPDATED = "integration.metadata_updated"
    INTEGRATION_EXTERNAL_ID_UPDATED = "integration.external_id_updated"
    INTEGRATION_TOKEN_EXPIRED = "integration.token_expired"
    INTEGRATION_DELETED = "integration.deleted"
    BUSINESS_CREATED = "business.created"
    BUSINESS_UPDATED = "business.updated"
    BUSINESS_DELETION_REQUESTED = "business.deletion_requested"
    BUSINESS_DELETION_CANCELED = "business.deletion_canceled"
    BUSINESS_NOT_OWNER_BLOCKED = "business.not_owner_blocked"
    BUSINESS_SELF_DELETED = "business.self_deleted"
    PROJECT_CREATED = "project.created"
    PROJECT_UPDATED = "project.updated"
    PROJECT_DELETED = "project.deleted"
    RPA_SCOPE_VIOLATION = "rpa.scope_violation"
    RPA_REVIEW_REPLIED = "rpa.review_replied"
    RPA_POST_PUBLISHED = "rpa.post_published"
    RPA_PHOTO_UPLOADED = "rpa.photo_uploaded"
    RPA_INFO_UPDATED = "rpa.info_updated"
    RPA_HOURS_UPDATED = "rpa.hours_updated"
    PLATFORM_POST_PUBLISHED = "platform.post_published"
    PLATFORM_DM_SENT = "platform.dm_sent"
    PLATFORM_REVIEW_REPLIED = "platform.review_replied"
    REVIEW_AUTO_REPLIED = "review.auto_replied"
    HITL_APPROVAL_RESOLVED = "hitl.approval_resolved"

    def visit(
        self,
        rbac_role_granted: typing.Callable[[], T_Result],
        rbac_member_removed: typing.Callable[[], T_Result],
        rbac_role_created: typing.Callable[[], T_Result],
        rbac_role_updated: typing.Callable[[], T_Result],
        rbac_role_deleted: typing.Callable[[], T_Result],
        rbac_invitation_created: typing.Callable[[], T_Result],
        rbac_invitation_revoked: typing.Callable[[], T_Result],
        rbac_invitation_accepted: typing.Callable[[], T_Result],
        auth_login_success: typing.Callable[[], T_Result],
        auth_login_failed: typing.Callable[[], T_Result],
        auth_logout: typing.Callable[[], T_Result],
        auth_password_changed: typing.Callable[[], T_Result],
        auth_user_registered: typing.Callable[[], T_Result],
        integration_connected: typing.Callable[[], T_Result],
        integration_disconnected: typing.Callable[[], T_Result],
        integration_token_rotated: typing.Callable[[], T_Result],
        integration_token_decrypted: typing.Callable[[], T_Result],
        integration_metadata_updated: typing.Callable[[], T_Result],
        integration_external_id_updated: typing.Callable[[], T_Result],
        integration_token_expired: typing.Callable[[], T_Result],
        integration_deleted: typing.Callable[[], T_Result],
        business_created: typing.Callable[[], T_Result],
        business_updated: typing.Callable[[], T_Result],
        business_deletion_requested: typing.Callable[[], T_Result],
        business_deletion_canceled: typing.Callable[[], T_Result],
        business_not_owner_blocked: typing.Callable[[], T_Result],
        business_self_deleted: typing.Callable[[], T_Result],
        project_created: typing.Callable[[], T_Result],
        project_updated: typing.Callable[[], T_Result],
        project_deleted: typing.Callable[[], T_Result],
        rpa_scope_violation: typing.Callable[[], T_Result],
        rpa_review_replied: typing.Callable[[], T_Result],
        rpa_post_published: typing.Callable[[], T_Result],
        rpa_photo_uploaded: typing.Callable[[], T_Result],
        rpa_info_updated: typing.Callable[[], T_Result],
        rpa_hours_updated: typing.Callable[[], T_Result],
        platform_post_published: typing.Callable[[], T_Result],
        platform_dm_sent: typing.Callable[[], T_Result],
        platform_review_replied: typing.Callable[[], T_Result],
        review_auto_replied: typing.Callable[[], T_Result],
        hitl_approval_resolved: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AuditAction.RBAC_ROLE_GRANTED:
            return rbac_role_granted()
        if self is AuditAction.RBAC_MEMBER_REMOVED:
            return rbac_member_removed()
        if self is AuditAction.RBAC_ROLE_CREATED:
            return rbac_role_created()
        if self is AuditAction.RBAC_ROLE_UPDATED:
            return rbac_role_updated()
        if self is AuditAction.RBAC_ROLE_DELETED:
            return rbac_role_deleted()
        if self is AuditAction.RBAC_INVITATION_CREATED:
            return rbac_invitation_created()
        if self is AuditAction.RBAC_INVITATION_REVOKED:
            return rbac_invitation_revoked()
        if self is AuditAction.RBAC_INVITATION_ACCEPTED:
            return rbac_invitation_accepted()
        if self is AuditAction.AUTH_LOGIN_SUCCESS:
            return auth_login_success()
        if self is AuditAction.AUTH_LOGIN_FAILED:
            return auth_login_failed()
        if self is AuditAction.AUTH_LOGOUT:
            return auth_logout()
        if self is AuditAction.AUTH_PASSWORD_CHANGED:
            return auth_password_changed()
        if self is AuditAction.AUTH_USER_REGISTERED:
            return auth_user_registered()
        if self is AuditAction.INTEGRATION_CONNECTED:
            return integration_connected()
        if self is AuditAction.INTEGRATION_DISCONNECTED:
            return integration_disconnected()
        if self is AuditAction.INTEGRATION_TOKEN_ROTATED:
            return integration_token_rotated()
        if self is AuditAction.INTEGRATION_TOKEN_DECRYPTED:
            return integration_token_decrypted()
        if self is AuditAction.INTEGRATION_METADATA_UPDATED:
            return integration_metadata_updated()
        if self is AuditAction.INTEGRATION_EXTERNAL_ID_UPDATED:
            return integration_external_id_updated()
        if self is AuditAction.INTEGRATION_TOKEN_EXPIRED:
            return integration_token_expired()
        if self is AuditAction.INTEGRATION_DELETED:
            return integration_deleted()
        if self is AuditAction.BUSINESS_CREATED:
            return business_created()
        if self is AuditAction.BUSINESS_UPDATED:
            return business_updated()
        if self is AuditAction.BUSINESS_DELETION_REQUESTED:
            return business_deletion_requested()
        if self is AuditAction.BUSINESS_DELETION_CANCELED:
            return business_deletion_canceled()
        if self is AuditAction.BUSINESS_NOT_OWNER_BLOCKED:
            return business_not_owner_blocked()
        if self is AuditAction.BUSINESS_SELF_DELETED:
            return business_self_deleted()
        if self is AuditAction.PROJECT_CREATED:
            return project_created()
        if self is AuditAction.PROJECT_UPDATED:
            return project_updated()
        if self is AuditAction.PROJECT_DELETED:
            return project_deleted()
        if self is AuditAction.RPA_SCOPE_VIOLATION:
            return rpa_scope_violation()
        if self is AuditAction.RPA_REVIEW_REPLIED:
            return rpa_review_replied()
        if self is AuditAction.RPA_POST_PUBLISHED:
            return rpa_post_published()
        if self is AuditAction.RPA_PHOTO_UPLOADED:
            return rpa_photo_uploaded()
        if self is AuditAction.RPA_INFO_UPDATED:
            return rpa_info_updated()
        if self is AuditAction.RPA_HOURS_UPDATED:
            return rpa_hours_updated()
        if self is AuditAction.PLATFORM_POST_PUBLISHED:
            return platform_post_published()
        if self is AuditAction.PLATFORM_DM_SENT:
            return platform_dm_sent()
        if self is AuditAction.PLATFORM_REVIEW_REPLIED:
            return platform_review_replied()
        if self is AuditAction.REVIEW_AUTO_REPLIED:
            return review_auto_replied()
        if self is AuditAction.HITL_APPROVAL_RESOLVED:
            return hitl_approval_resolved()
