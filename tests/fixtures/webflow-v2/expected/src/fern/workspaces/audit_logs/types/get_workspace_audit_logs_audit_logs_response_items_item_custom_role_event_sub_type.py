

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType(enum.StrEnum):
    ROLE_CREATED = "role_created"
    ROLE_UPDATED = "role_updated"
    ROLE_DELETED = "role_deleted"

    def visit(
        self,
        role_created: typing.Callable[[], T_Result],
        role_updated: typing.Callable[[], T_Result],
        role_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType.ROLE_CREATED:
            return role_created()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType.ROLE_UPDATED:
            return role_updated()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType.ROLE_DELETED:
            return role_deleted()
