

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType(enum.StrEnum):
    USER_ADDED = "user_added"
    USER_REMOVED = "user_removed"
    USER_ROLE_UPDATED = "user_role_updated"
    USER_GRANULAR_ACCESS_UPDATED = "user_granular_access_updated"

    def visit(
        self,
        user_added: typing.Callable[[], T_Result],
        user_removed: typing.Callable[[], T_Result],
        user_role_updated: typing.Callable[[], T_Result],
        user_granular_access_updated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType.USER_ADDED:
            return user_added()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType.USER_REMOVED:
            return user_removed()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType.USER_ROLE_UPDATED:
            return user_role_updated()
        if (
            self
            is GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType.USER_GRANULAR_ACCESS_UPDATED
        ):
            return user_granular_access_updated()
