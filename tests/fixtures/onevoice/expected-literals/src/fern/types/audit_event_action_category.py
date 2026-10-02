

import typing

AuditEventActionCategory = typing.Union[
    typing.Literal["rbac", "auth", "integration", "business", "project", "rpa", "platform", "review", "hitl", "other"],
    typing.Any,
]
