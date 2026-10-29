

import typing

GetWorkspaceAuditLogsAuditLogsRequestEventType = typing.Union[
    typing.Literal[
        "user_access",
        "custom_role",
        "workspace_membership",
        "site_membership",
        "workspace_invitation",
        "workspace_setting",
    ],
    typing.Any,
]
