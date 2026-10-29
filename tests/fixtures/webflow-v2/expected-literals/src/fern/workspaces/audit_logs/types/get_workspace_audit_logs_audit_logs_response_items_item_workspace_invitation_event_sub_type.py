

import typing

GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType = typing.Union[
    typing.Literal[
        "invite_sent",
        "invite_accepted",
        "invite_updated",
        "invite_canceled",
        "invite_declined",
        "access_request_accepted",
    ],
    typing.Any,
]
