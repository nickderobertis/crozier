

import typing

AclObjectType = typing.Union[
    typing.Literal[
        "organization",
        "project",
        "experiment",
        "dataset",
        "prompt",
        "prompt_session",
        "group",
        "role",
        "org_member",
        "project_log",
        "org_project",
    ],
    typing.Any,
]
