

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType(enum.StrEnum):
    INVITE_SENT = "invite_sent"
    INVITE_ACCEPTED = "invite_accepted"
    INVITE_UPDATED = "invite_updated"
    INVITE_CANCELED = "invite_canceled"
    INVITE_DECLINED = "invite_declined"
    ACCESS_REQUEST_ACCEPTED = "access_request_accepted"

    def visit(
        self,
        invite_sent: typing.Callable[[], T_Result],
        invite_accepted: typing.Callable[[], T_Result],
        invite_updated: typing.Callable[[], T_Result],
        invite_canceled: typing.Callable[[], T_Result],
        invite_declined: typing.Callable[[], T_Result],
        access_request_accepted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.INVITE_SENT:
            return invite_sent()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.INVITE_ACCEPTED:
            return invite_accepted()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.INVITE_UPDATED:
            return invite_updated()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.INVITE_CANCELED:
            return invite_canceled()
        if self is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.INVITE_DECLINED:
            return invite_declined()
        if (
            self
            is GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType.ACCESS_REQUEST_ACCEPTED
        ):
            return access_request_accepted()
