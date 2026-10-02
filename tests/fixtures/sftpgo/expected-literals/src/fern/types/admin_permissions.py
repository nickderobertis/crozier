

import typing

AdminPermissions = typing.Union[
    typing.Literal[
        "*",
        "add_users",
        "edit_users",
        "del_users",
        "view_users",
        "view_conns",
        "close_conns",
        "view_status",
        "manage_folders",
        "manage_groups",
        "quota_scans",
        "manage_defender",
        "view_defender",
        "view_events",
        "disable_mfa",
    ],
    typing.Any,
]
