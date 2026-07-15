

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IssueTrackingEventType(str, enum.Enum):
    ALL = "*"
    ISSUE_TRACKING_TICKET_CREATED = "issue-tracking.ticket.created"
    ISSUE_TRACKING_TICKET_UPDATED = "issue-tracking.ticket.updated"
    ISSUE_TRACKING_TICKET_DELETED = "issue-tracking.ticket.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        issue_tracking_ticket_created: typing.Callable[[], T_Result],
        issue_tracking_ticket_updated: typing.Callable[[], T_Result],
        issue_tracking_ticket_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IssueTrackingEventType.ALL:
            return all_()
        if self is IssueTrackingEventType.ISSUE_TRACKING_TICKET_CREATED:
            return issue_tracking_ticket_created()
        if self is IssueTrackingEventType.ISSUE_TRACKING_TICKET_UPDATED:
            return issue_tracking_ticket_updated()
        if self is IssueTrackingEventType.ISSUE_TRACKING_TICKET_DELETED:
            return issue_tracking_ticket_deleted()
