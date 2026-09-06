

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType(enum.StrEnum):
    USER_ADDED = "user_added"
    USER_REMOVED = "user_removed"
    USER_ROLE_UPDATED = "user_role_updated"

    def visit(
        self,
        user_added: typing.Callable[[], T_Result],
        user_removed: typing.Callable[[], T_Result],
        user_role_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType.USER_ADDED:
            return user_added()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType.USER_REMOVED:
            return user_removed()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType.USER_ROLE_UPDATED:
            return user_role_updated()
