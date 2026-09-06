

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AclListPermission(enum.StrEnum):
    """
    Each permission permits a certain type of operation on an object in the system

    Permissions can be assigned to to objects on an individual basis, or grouped into roles
    """

    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    CREATE_ACLS = "create_acls"
    READ_ACLS = "read_acls"
    UPDATE_ACLS = "update_acls"
    DELETE_ACLS = "delete_acls"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        read: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        create_acls: typing.Callable[[], T_Result],
        read_acls: typing.Callable[[], T_Result],
        update_acls: typing.Callable[[], T_Result],
        delete_acls: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AclListPermission.CREATE:
            return create()
        if self is AclListPermission.READ:
            return read()
        if self is AclListPermission.UPDATE:
            return update()
        if self is AclListPermission.DELETE:
            return delete()
        if self is AclListPermission.CREATE_ACLS:
            return create_acls()
        if self is AclListPermission.READ_ACLS:
            return read_acls()
        if self is AclListPermission.UPDATE_ACLS:
            return update_acls()
        if self is AclListPermission.DELETE_ACLS:
            return delete_acls()
