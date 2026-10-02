

import typing

IssueTrackingEventType = typing.Union[
    typing.Literal[
        "*", "issue-tracking.ticket.created", "issue-tracking.ticket.updated", "issue-tracking.ticket.deleted"
    ],
    typing.Any,
]
