

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType(enum.StrEnum):
    LOGIN = "login"
    LOGOUT = "logout"

    def visit(self, login: typing.Callable[[], T_Result], logout: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType.LOGIN:
            return login()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType.LOGOUT:
            return logout()
