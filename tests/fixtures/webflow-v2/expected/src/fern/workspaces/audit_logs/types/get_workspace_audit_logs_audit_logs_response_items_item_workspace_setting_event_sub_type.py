

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType(enum.StrEnum):
    SETTING_UPDATED = "setting_updated"

    def visit(self, setting_updated: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType.SETTING_UPDATED:
            return setting_updated()
