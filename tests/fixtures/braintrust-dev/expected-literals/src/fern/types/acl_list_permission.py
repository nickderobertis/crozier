

import typing

AclListPermission = typing.Union[
    typing.Literal["create", "read", "update", "delete", "create_acls", "read_acls", "update_acls", "delete_acls"],
    typing.Any,
]
