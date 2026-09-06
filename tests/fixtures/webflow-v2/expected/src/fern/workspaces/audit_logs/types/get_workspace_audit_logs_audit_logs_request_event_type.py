

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsRequestEventType(enum.StrEnum):
    USER_ACCESS = "user_access"
    CUSTOM_ROLE = "custom_role"
    WORKSPACE_MEMBERSHIP = "workspace_membership"
    SITE_MEMBERSHIP = "site_membership"
    WORKSPACE_INVITATION = "workspace_invitation"
    WORKSPACE_SETTING = "workspace_setting"

    def visit(
        self,
        user_access: typing.Callable[[], T_Result],
        custom_role: typing.Callable[[], T_Result],
        workspace_membership: typing.Callable[[], T_Result],
        site_membership: typing.Callable[[], T_Result],
        workspace_invitation: typing.Callable[[], T_Result],
        workspace_setting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.USER_ACCESS:
            return user_access()
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.CUSTOM_ROLE:
            return custom_role()
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.WORKSPACE_MEMBERSHIP:
            return workspace_membership()
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.SITE_MEMBERSHIP:
            return site_membership()
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.WORKSPACE_INVITATION:
            return workspace_invitation()
        if self is GetWorkspaceAuditLogsAuditLogsRequestEventType.WORKSPACE_SETTING:
            return workspace_setting()
